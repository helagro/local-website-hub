from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import env
import fileinput
from pathlib import Path
import subprocess

mainWebsiteFolderPath = os.path.dirname(os.path.dirname(__file__)) + "/localWebsites" if not hasattr(env, "customMainWebsiteFolderPath") else getattr(env, "customMainWebsiteFolderPath")

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
        fillInfoFile()
        return root + '/index.html'
    elif path == "/update":
        updateWebsites()
        return 'static/updated.html'

    for website in env.localWebsiteDirs:
        if(path == "/" + website.name):
            root = website.path
            return getFullPath("/")

    pathIfIsInGithubFolder = mainWebsiteFolderPath + path
    if os.path.isdir(pathIfIsInGithubFolder):
        root = pathIfIsInGithubFolder
        return getFullPath("/")
    
    return filename


def fillInfoFile():
    f = open("static/addedWebsites.js", "w")

    f.write("addedWebsites=[")
    for website in env.localWebsiteDirs:
        websiteArrString = '"{0}",'.format(website.name)
        f.write(websiteArrString)
    f.write("]")
    f.close()   


def updateWebsites():
    for website in env.localWebsiteDirs:
        subprocess.run(["git", "-C", website.path, "pull"])
        subprocess.run(["git", "-C", website.path, "pull", "--recurse-submodules"])


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