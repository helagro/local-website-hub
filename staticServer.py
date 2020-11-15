from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import env

class StaticServer(BaseHTTPRequestHandler):
   
    def do_GET(self):
        filename = getFullPath(self.path)

        self.send_response(200)
        header = getHeader(filename)
        self.send_header('Content-type', header)
        self.end_headers()

        with open(filename, 'rb') as fh:
            html = fh.read()
            #html = bytes(html, 'utf8')
            self.wfile.write(html)


root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

def getFullPath(path):
    global root
    filename = root + path

    if path == '/':
        filename = root + '/index.html'
    
    #replace with your own names
    elif path == "/day-eval":
        #replace with your own website root paths 
        root = env.dayEvalRoot
        return getFullPath("/")
    elif path == "/pause-checklist":
        root = env.pauseChecklist
        return getFullPath("/")

    return filename


def getHeader(filename):
    header = "text/html"
    if filename[-4:] == '.css':
        header = 'text/css'
    elif filename[-5:] == '.json':
        header = 'application/javascript'
    elif filename[-3:] == '.js':
        header = 'application/javascript'
    elif filename[-4:] == '.ico':
        header = 'image/x-icon'
    
    return header