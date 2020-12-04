from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import env
import fileinput
from pathlib import Path
import subprocess
import fileManager

mainWebsiteFolderPath = os.path.dirname(os.path.dirname(__file__)) + "/localWebsites" if not hasattr(env, "customMainWebsiteFolderPath") else getattr(env, "customMainWebsiteFolderPath")
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

class StaticServer(BaseHTTPRequestHandler):
   
    def do_GET(self):
        filename = getFullPath(self.path)

        self.send_response(200)
        header = getHeader(filename)
        self.send_header('Content-type', header)
        self.end_headers()

        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)


def getFullPath(path):
    global root
    filename = root + path

    if path == '/':
        indexPath = root + "/index.html"
        if os.path.isfile(indexPath):
            return indexPath

        return "static/index.html"
    elif path == "/update":
        updateWebsites(root)
        return 'static/updated.html'

    pathIfInLocalWebsiteFolder = mainWebsiteFolderPath + path
    if os.path.isdir(pathIfInLocalWebsiteFolder):
        root = pathIfInLocalWebsiteFolder
        return getFullPath("/")
    
    return filename


def generateDirInfoPage(dir):
    dirs = fileManager.getFolders(dir)
    fileManager.fillEntriesArray("static/dirsInPath.js")


def updateWebsites(dir):
    folders = fileManager.getFolders(dir)

    for website in folders:
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