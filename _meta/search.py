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



"""

import json
import os
import pathlib
import sqlite3
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Install pip=beautifulsoup4", file=sys.stderr)

def create(path=":memory:"):
    """Create new database and return the connection object"""

    if not os.path.exists('_build/dirhtml'):
        print("You must `make dirhtml` first.", file=sys.stderr)
    print("Creating database", file=sys.stderr)
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS pages"
        " USING fts5(path, title, body"
        ", tokenize = 'porter unicode61'"
        " );")
    conn.commit()

    from html.parser import HTMLParser
    class HTMLFilter(HTMLParser):
        text = ""
        def handle_data(self, data):
            self.text += data


    root = pathlib.Path("_build/dirhtml")
    for file in root.glob('**/*.html'):
        relpath = file.relative_to(root).parent

        raw = file.open().read()
        contents =  BeautifulSoup(raw, 'html.parser')
        title = contents.title.contents[0]
        #contents = contents.get_text()
        contents = contents.find('div', {'class': 'document'}).get_text()

        contents = ' '.join(contents.split())
        #print(relpath, repr(contents)[:50])

        #f = HTMLFilter()
        #f.feed(raw)
        #print(f.text)

        conn.execute('INSERT INTO pages VALUES (?, ?, ?)', (str(relpath), title, contents))
    conn.commit()
    print("Done: creating database", file=sys.stderr)
    return conn

def search(conn, term, tokens=64, limit=10):
    """Do a single search and return snipets"""
    #term = f"NEAR({term})"
    print('Searching:', term)
    cur = conn.execute(
        "SELECT path, rank, snippet(pages, 2, '', '', '', ?)"
        " FROM pages WHERE pages"
        " MATCH ?"
        " ORDER BY rank"
        " LIMIT ?", (tokens, term, limit))
    for result in cur.fetchall():
        yield result

def serve(conn):
    """Start a HTTP server and return snipets"""
    import http.server
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            terms = self.path.strip('/')
            terms = ' '.join(terms.split('%20'))
            #print(terms)
            data = list(search(conn, terms))
            self.wfile.write(json.dumps(data).encode())

    server_class = http.server.HTTPServer
    handler_class = Handler
    server_address = ('', 8000)
    print(f"Server running on {server_address}", file=sys.stderr)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()



import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--db', default=':memory:')
parser.add_argument('mode')
parser.add_argument('searchterms', nargs='*')
args = parser.parse_args()

if args.mode == 'create' or args.db == ':memory:':
    conn = create(args.db)
else:
    conn = sqlite3.connect(args.db)

if args.mode == 'serve':
    serve(conn)
if args.mode == 'search':
    for line in search(conn, " ".join(args.searchterms)):
        print(line)
