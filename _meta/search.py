"""
Simple search API for these docs

Usage:
    make dirhtml
    pip install beautifulsoup4
    python _meta/search.py serve
    curl https://localhost/array+job

To not re-create the database each time:
    python _meta/search.py create --db=search.db
    python _meta/search.py serve --db=search.db

Searching: `a+b` means a and b right next to each other.

Web API:
GET /?q=QUERY        return this QUERY
GET /?limit=N        this many items returned
GET /?raw=true       query already in fts5 syntax:
                       https://www.sqlite.org/fts5.html#full_text_query_syntax
POST /               update database (basic auth, env var SEARCH_UPDATE_AUTHORIZATION)

"""

BASE = 'https://scicomp.aalto.fi/'

import base64
import copy
import hmac
import json
import os
import pathlib
import sqlite3
import sys
import time
import urllib.parse
import urllib.request


def html2text(s):
    contents = s.get_text()
    #contents = ' '.join(contents.split())
    #contents = re.sub(r'\n+', '\n', contents)
    return contents



def create(path=":memory:"):
    """Create new database and return the connection object."""
    print("Creating database", file=sys.stderr)
    conn = sqlite3.connect(path)
    conn.row_factory = dict_factory
    conn.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS pages"
        " USING fts5(path, title, body, time_update"
        ", tokenize = 'porter unicode61'"
        " );")
    conn.commit()
    return conn



def insert(conn, data):
    """Insert data into the database.

    Data is iterable of relpath, title, body.
    """
    time_start = time.time()

    for relpath, title, section_body in data:
        conn.execute('INSERT INTO pages VALUES (?, ?, ?, ?)', (relpath, title, section_body, time.time()))

    conn.execute('DELETE FROM pages WHERE time_update<?', (time_start,))
    conn.execute("INSERT INTO pages(pages, rank) VALUES('automerge', 8)")
    conn.commit()
    conn.execute('VACUUM;')
    print("Done: creating database", file=sys.stderr)




def get_data():
    """Iterate over (path, data, value) fields.

    Returns iterable of data which can be inserted into the database.
    """
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("Install pip=beautifulsoup4", file=sys.stderr)


    if not os.path.exists('_build/dirhtml'):
        print("You must `make dirhtml` first.", file=sys.stderr)

    from html.parser import HTMLParser
    class HTMLFilter(HTMLParser):
        text = ""
        def handle_data(self, data):
            self.text += data

    root = pathlib.Path("_build/dirhtml")
    for file in root.glob('**/*.html'):
        relpath = str(file.relative_to(root).parent) + '/'

        raw = file.open().read()
        contents =  BeautifulSoup(raw, 'html.parser')
        title = contents.title.contents[0]
        body = contents.find('div', {'class': 'document'})
        body = html2text(body)

        body = contents.findAll('section')
        print(relpath)
        for section in body:
            # skip outer container
            if 'wy-nav-content-wrap' in section.attrs.get('class', []):
                continue
            # Find relative path link
            relpath2 = relpath
            id_ = section.attrs.get('id', 'no-section')
            if id_:
                relpath2 += '#'+id_
            # Remove subsections and other unuseful stuff
            section = copy.copy(section)
            if x := section.find('footer'):
                x.clear()
            if x := section.find('div', {'class': 'rst-footer-buttons'}):
                x.clear()
            for subsec in section.findAll('section'):
                subsec.clear()
            section_body = html2text(section)
            #print(f"  {relpath2:50}, {repr(section_body)[:150]}")
            yield (relpath2, title, section_body)



def search(conn, query, tokens=64, limit=10, raw=False):
    """Do a single search and yield snipets.


    raw: if true (default false), the query is already in a sqlite3 fts5 search syntax:
           https://www.sqlite.org/fts5.html#full_text_query_syntax
         if false, then quote the tokens to prevent sytax errors.  Form of quoting
         may change in the future.

    limit: number of results returned (default 10)

    tokens: number of tokens around the snipet (default 64)

    """
    if not raw:
        #query = f"NEAR({query})"
        #query = f'{{title body}} : {query}'
        query = ' '.join(f'"{x}"' for x in (y.replace('"', '""') for y in query.split()))
    print('Searching:', repr(query))
    cur = conn.execute(
        f"SELECT :base||path AS path, rank, snippet(pages, 2, '', '', '', :tokens) AS snipet, body"
        " FROM pages WHERE"
        " body MATCH :query"
        " ORDER BY rank"
        " LIMIT :limit", dict(tokens=tokens, query=query, limit=limit, base=BASE))
    for result in cur.fetchall():
        yield result

def serve(conn, bind=':8000'):
    """Start a HTTP server and serve snipets."""
    import http.server
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            """Accept updates if token-authenticated"""
            print(f"Updating database from {self.client_address}")
            mode, auth = self.headers.get("Authorization", "").split(' ', 1)
            user, token = base64.b64decode(auth).decode().split(':')
            print(mode, auth, user, token)
            if (mode == 'Basic'
                and len(token) > 20
                and hmac.compare_digest(token, os.environ.get('SEARCH_UPDATE_AUTHORIZATION', ''))
                ):
                data_bytes = int(self.headers.get("Content-Length"), 0)
                data = json.loads(self.rfile.read(data_bytes))
                create(data)
                #create(data, conn)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps('{}').encode())
                return
            self.send_response(405)


        def do_GET(self):
            """Serve results"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            url = urllib.parse.urlparse(self.path)
            path = url.path
            qs = urllib.parse.parse_qs(url.query)
            query = None
            raw = False
            limit = 10
            if 'q' in qs:
                query = qs['q'][0]
                if 'raw' in qs:
                    raw = True
                if 'limit' in qs:
                    limit = qs['limit'][0]
            elif path != '/':
                query = self.path.strip('/')
                query = urllib.parse.unquote(query)
            else:
                self.wfile.write(b'{"error": "specify search query as q="}')
                return
            #print(query)
            data = list(search(conn, query, raw=raw, limit=limit))
            self.wfile.write(json.dumps(data).encode())

    server_class = http.server.HTTPServer
    handler_class = Handler
    server_address = bind.split(':')[0], int(bind.split(':')[1])
    print(f"Server running on {server_address}", file=sys.stderr)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def dict_factory(cur, row):
    """sqlite3 helper to return dicts of each row.  Used in connection initialization"""
    fields = [col[0] for col in cur.description]
    return {key: value for key, value in zip(fields, row)}


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', default=':memory:')
    parser.add_argument('--bind', default=':8000')
    parser.add_argument('--limit', default=10, type=int)
    parser.add_argument('mode')
    parser.add_argument('query', nargs='*')
    args = parser.parse_args()

    # Make database, insert data if it is temporary.
    conn = create(args.db)
    if args.db == ':memory:' and args.mode != 'update':
        insert(conn, get_data())

    if args.mode == 'create':
        insert(conn, get_data())
    if args.mode == 'serve':
        serve(conn, bind=args.bind)
    if args.mode == 'search':
        for line in search(conn, " ".join(args.query), limit=args.limit):
            print(line)
    if args.mode == 'update':
        url = args.query[0]
        data = list(get_data())
        token = os.environ.get('SEARCH_UPDATE_AUTHORIZATION', '')
        import requests
        requests.post(url, data=json.dumps(data), auth=('', token), timeout=60)


if __name__ == '__main__':
    main()
