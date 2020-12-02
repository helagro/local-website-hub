from http.server import HTTPServer, BaseHTTPRequestHandler
from staticServer import StaticServer
import env

address = "" if not hasattr(env, "websiteAddress") else getattr(env, "websiteAddress")

def main():
    runServer()

def runServer(server_class=HTTPServer, handler_class=StaticServer, port=9991):
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on {0} port {1}'.format(address, port))
    httpd.serve_forever()

main()