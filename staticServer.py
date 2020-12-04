from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import env
import fileinput
from pathlib import Path
import subprocess
import fileManager
from urllib import parse

mainWebsiteFolderPath = os.path.dirname(os.path.dirname(__file__)) + "/localWebsites" if not hasattr(env, "customMainWebsiteFolderPath") else getattr(env, "customMainWebsiteFolderPath")

class StaticServer(BaseHTTPRequestHandler):
   
    def do_GET(self):
        attr = parse.parse_qs(parse.urlsplit(self.path).query)
        pathWithoutAttr = self.path.split("?")[0]
        filename = getFullPath(pathWithoutAttr, attr)
        
        if os.path.isdir(filename):
            self.send_response(301)

            if os.path.isfile(filename + "/index.html"):
                self.send_header("Location", pathWithoutAttr + "/index.html")
            else:
                self.send_header("Location", "/local-website-hub?p=" + filename)

            self.end_headers()
            return
            

        self.send_response(200)
        header = getHeader(filename)
        self.send_header('Content-type', header)
        self.end_headers()

        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)


def getFullPath(path, attr):
    splittedPath = path.split("/")
    if(splittedPath[1].startswith("local-website-hub")):  
        if(len(splittedPath) == 2):
            p = mainWebsiteFolderPath if (not "p" in attr) else attr["p"][0]

            generateDirInfoPage(p)
            return os.path.dirname(__file__) + "/static/"

        return os.path.dirname(__file__) + "/static/" + splittedPath[2]

    return mainWebsiteFolderPath + path


def generateDirInfoPage(dir):
    dirs = fileManager.getFolders(dir)
    fileManager.fillDirInfoFile("static/dirsInPath.js", dirs, dir)

    return "static/index.html"


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
    elif filename[-4:] == '.svg':
        header = 'image/svg+xml'
    
    return header