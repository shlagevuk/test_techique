#!/usr/bin/env python
from elasticsearch import Elasticsearch
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
from collections import defaultdict
import SocketServer

ES_HOST="localhost"
ES_PORT=9200
#methode safe
#ES_INDEX=""
#methode non-safe:
#on peut changer l'index via un param d'url
class S(BaseHTTPRequestHandler):
    es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])

    def do_GET(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        parsed_args=parse_qs(self.path[2:])

        if 'id' in parsed_args:
            id_search = parsed_args['id'][0]
            try:
                int(id_search)
            except:
                self.send_response(500, "id is not an int")
                self.wfile.write("")
                return(1)
        else:
            id_search = 1

        if 'index' in parsed_args:
            index_search=parsed_args['index'][0]
            index_search.decode("utf8","ignore")
        else:
            index_search='dealer.csv'

        try:
            result_es= self.es.get(index=index_search, doc_type='text', id=id_search)
            self.send_response(200)
            self.wfile.write(result_es)
        except:
            self.send_response(404, "id not found")
            self.wfile.write("")

    def do_HEAD(self):
        self.send_response(200)

    def do_POST(self):
        # Doesn't do anything with posted data
        self.send_response(404)
        self.wfile.write("<html><body><h1>NO POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
