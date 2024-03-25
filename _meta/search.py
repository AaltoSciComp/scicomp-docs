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
GET /?operator=OP    Use this search operator (default OR)
                       AND, OR, NEAR, '' (html: %20), or '+' (html: %2b)
POST /               update database (basic auth, env var SEARCH_UPDATE_AUTHORIZATION)

"""

SITE = 'https://scicomp.aalto.fi/'
OPERATOR_DEFAULT = 'OR'

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


def textify(s):
    """html to text, local attempt"""
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
        " USING fts5(site, path, title, time_update, body, html, markdown"
        ", tokenize = 'porter unicode61'"
        " );")
    conn.commit()
    return conn




def insert(conn, data, site):
    """Insert data into the database.

    Data is iterable of relpath, title, body.
    """
    time_start = time.time()
    for row in data:
        for format in ('html', 'markdown'):
            if format not in row:
                row[format] = None
        row['time_update'] = time_start
        conn.execute('INSERT INTO pages'
                     '(site, path, title, time_update, body, html, markdown)'
                     ' VALUES (:site, :path, :title, :time_update, :body, :html, :markdown)', row)

    conn.execute('DELETE FROM pages WHERE site=? and time_update<?', (site, time_start,))
    conn.execute("INSERT INTO pages(pages, rank) VALUES('automerge', 8)")
    conn.commit()
    conn.execute('VACUUM;')
    print("Done: creating database", file=sys.stderr)




def get_data(site, dirhtml_dir='_build/dirhtml'):
    """Iterate over (path, data, value) fields.

    Returns iterable of data which can be inserted into the database.
    """
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("Install pip=beautifulsoup4", file=sys.stderr)
    from markdownify import markdownify
    #import html2text

    if not os.path.exists(dirhtml_dir):
        print(f"You must `make dirhtml` first, {dirhtml_dir} is empty, or use --dirhtml", file=sys.stderr)

    from html.parser import HTMLParser
    class HTMLFilter(HTMLParser):
        text = ""
        def handle_data(self, data):
            self.text += data

    root = pathlib.Path(dirhtml_dir)
    for file in root.glob('**/*.html'):
        relpath = str(file.relative_to(root).parent) + '/'
        print(relpath)

        raw = file.open().read()
        contents =  BeautifulSoup(raw, 'html.parser')
        if not hasattr(contents.title, 'contents'):
            # These are often stub pages.  Ignore.
            continue
        title = contents.title.contents[0]
        body = contents.find('div', {'class': 'document'})
        body = textify(body)

        body = contents.findAll('section')
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
            for x in section.findAll('a', {'class': 'headerlink'}):
                x.clear()
            for subsec in section.findAll('section'):
                subsec.clear()
            #import pdb ; pdb.set_trace()
            section_body = textify(section)
            section_html = str(section)
            # underlined titles, ``` blocks
            section_md = markdownify(str(section), heading_style='ATX')
            # '#' titles, indented blocks
            #section_md = html2text(str(section))
            #print(f"  {relpath2:50}, {repr(section_body)[:150]}")
            yield dict(site=site, path=site+relpath2, title=title, body=section_body,
                       html=section_html, markdown=section_md)



def search(conn, query, tokens=64, limit=10, raw=False, operator=OPERATOR_DEFAULT, site=None):
    """Do a single search and yield snipets.


    raw: if true (default false), the query is already in a sqlite3 fts5 search syntax:
           https://www.sqlite.org/fts5.html#full_text_query_syntax
         if false, then quote the tokens to prevent sytax errors.  Form of quoting
         may change in the future.

    limit: number of results returned (default 10)

    tokens: number of tokens around the snipet (default 64)

    """
    if not raw:
        operator = operator.upper()
        if operator not in {'NEAR', 'OR', 'AND', '+', ' ', ''}:
            raise ValueError(f"Not allowed operator: {operator}")
        if isinstance(query, str):
            query = query.split()
        #query = f"NEAR({query})"
        #query = f'{{title body}} : {query}'
        near = False
        if operator == 'NEAR':
            operator = ''
            near = True
        query = f' {operator} '.join(f'"{x}"' for x in (y.replace('"', '""') for y in query))
        if near:
            query = f'NEAR( {query} )'
    print('Searching:', repr(query), file=sys.stderr)
    cur = conn.execute(
        " ".join([
            "SELECT path AS path, rank, snippet(pages, 4, '', '', '', :tokens) AS snipet, body, html, markdown",
            " FROM pages WHERE",
            " body MATCH :query",
            " and site = :site" if site else "",
            " ORDER BY rank",
            " LIMIT :limit"]), dict(tokens=tokens, query=query, limit=limit, site=site))
    for result in cur.fetchall():
        yield result

def serve(conn, bind=':8000', operator=OPERATOR_DEFAULT):
    """Start a HTTP server and serve snipets."""
    import http.server
    class Handler(http.server.BaseHTTPRequestHandler):

        def do_GET(self, operator=operator):
            """Serve results"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            url = urllib.parse.urlparse(self.path)
            path = url.path
            qs = urllib.parse.parse_qs(url.query)
            query = None
            raw = False
            limit = 10
            site = None
            if 'q' in qs:
                query = qs['q'][0]
                if 'raw' in qs:
                    raw = True
                if 'limit' in qs:
                    limit = qs['limit'][0]
                if 'operator' in qs:
                    operator = qs['operator'][0]
                if 'site' in qs:
                    site = qs['site'][0]
            elif path != '/':
                query = self.path.strip('/')
                query = urllib.parse.unquote(query)
            else:
                time_update = conn.execute('select site, max(time_update) as tu from pages group by site').fetchall()
                time_update = {tu['site']: time.ctime(tu['tu']) for tu in time_update}
                self.wfile.write(b'{"error": "specify search query as q=", "time_update": %s}'%json.dumps(time_update).encode())
                return
            #print(query)
            data = list(search(conn, query, raw=raw, limit=limit, operator=operator, site=site))
            self.wfile.write(json.dumps(data).encode())

        def do_POST(self):
            """Accept updates if token-authenticated"""
            print(f"Updating database from {self.client_address}")
            mode, auth = self.headers.get("Authorization", "").split(' ', 1)
            user, token = base64.b64decode(auth).decode().split(':')
            #print(mode, auth, user, token)
            if (mode == 'Basic'
                and len(token) > 20
                and hmac.compare_digest(token, os.environ.get('SEARCH_UPDATE_AUTHORIZATION', ''))
                ):
                data_bytes = int(self.headers.get("Content-Length"), 0)
                data = json.loads(self.rfile.read(data_bytes))
                site = data['site']
                data = data['data']
                insert(conn, data, site)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps('{}').encode())
                return
            self.send_response(405)
            self.end_headers()


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
    parser.add_argument('--db', default=':memory:', help="default '%(default)s")
    parser.add_argument('--bind', default=':8000', help="default %(default)s")
    parser.add_argument('--operator', default=OPERATOR_DEFAULT)
    parser.add_argument('--limit', default=10, type=int)
    parser.add_argument('--site', default=SITE, help="Site name, should end in slash to be prepended to the page paths, default '%(default)s'")
    parser.add_argument('--dirhtml', default='_build/dirhtml', help="Location of Sphinx content (should be Sphinx dirhtml output, default '%(default)s'")
    parser.add_argument('mode', help="create, serve, search, update")
    parser.add_argument('query', nargs='*')
    args = parser.parse_args()

    # Make database, insert data if it is temporary.
    conn = create(args.db)
    if args.db == ':memory:' and args.mode != 'update':
        insert(conn, get_data(args.site, args.dirhtml), args.site)

    if args.mode == 'create':
        insert(conn, get_data(args.site, args.dirhtml), args.site)
    if args.mode == 'serve':
        serve(conn, bind=args.bind, operator=args.operator)
    if args.mode == 'search':
        print('[')
        for line in search(conn, args.query, limit=args.limit, operator=args.operator, site=args.site):
            print(json.dumps(line) + ',')
        print('null]')
    if args.mode == 'update':
        url = args.query[0]
        data = {
            'site': args.site,
            'data': list(get_data(args.site, args.dirhtml)),
            }
        token = os.environ.get('SEARCH_UPDATE_AUTHORIZATION', '')
        import requests
        data = json.dumps(data)
        print ("Update size:", len(data))
        response = requests.post(url, data=data, auth=('', token), timeout=60)
        print(response.status_code, response.reason)
        if response.status_code != 200:
            sys.exit(1)


if __name__ == '__main__':
    main()
