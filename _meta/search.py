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

BASE = 'https://scicomp.aalto.fi/'

import copy
import json
import os
import pathlib
import re
import sqlite3
import sys
from urllib.parse import unquote

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Install pip=beautifulsoup4", file=sys.stderr)

def html2text(s):
    contents = s.get_text()
    #contents = ' '.join(contents.split())
    #contents = re.sub(r'\n+', '\n', contents)
    return contents

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
        relpath = str(file.relative_to(root).parent) + '/'

        raw = file.open().read()
        contents =  BeautifulSoup(raw, 'html.parser')
        title = contents.title.contents[0]
        body = contents.find('div', {'class': 'document'})
        body = html2text(body)
        #conn.execute('INSERT INTO pages VALUES (?, ?, ?)', (relpath, title, body))
        #if relpath.startswith('triton/tut/array'):
        #    import pdb; pdb.set_trace()


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
            conn.execute('INSERT INTO pages VALUES (?, ?, ?)', (relpath2, title, section_body))

        #print(relpath, repr(contents)[:50])

        #f = HTMLFilter()
        #f.feed(raw)
        #print(f.text)

    conn.commit()
    print("Done: creating database", file=sys.stderr)
    return conn

def search(conn, query, tokens=64, limit=10):
    """Do a single search and return snipets"""
    #query = f"NEAR({query})"
    print('Searching:', query)
    cur = conn.execute(
        f"SELECT :base||path AS path, rank, snippet(pages, 2, '', '', '', :tokens) AS snipet, body"
        " FROM pages WHERE pages"
        " MATCH :query"
        " ORDER BY rank"
        " LIMIT :limit", dict(tokens=tokens, query=query, limit=limit, base=BASE))
    for result in cur.fetchall():
        yield result

def serve(conn, bind=':8000'):
    """Start a HTTP server and return snipets"""
    import http.server
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if self.path == '/':
                self.wfile.write(b'{"error": "specify search query as path"}')
            query = self.path.strip('/')
            query = unquote(query)
            #print(query)
            data = list(search(conn, query))
            self.wfile.write(json.dumps(data).encode())

    server_class = http.server.HTTPServer
    handler_class = Handler
    server_address = bind.split(':')[0], int(bind.split(':')[1])
    print(f"Server running on {server_address}", file=sys.stderr)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def dict_factory(cur, row):
    """sqlite3 helper to return dicts of each row"""
    fields = [col[0] for col in cur.description]
    return {key: value for key, value in zip(fields, row)}


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--db', default=':memory:')
parser.add_argument('--bind', default=':8000')
parser.add_argument('mode')
parser.add_argument('query', nargs='*')
args = parser.parse_args()

if args.mode == 'create' or args.db == ':memory:':
    conn = create(args.db)
else:
    conn = sqlite3.connect(args.db)
conn.row_factory = dict_factory

if args.mode == 'serve':
    serve(conn, bind=args.bind)
if args.mode == 'search':
    for line in search(conn, " ".join(args.query)):
        print(line)
