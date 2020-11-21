from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from staticServer import StaticServer


def runServer(server_class=HTTPServer, handler_class=StaticServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


runServer()
