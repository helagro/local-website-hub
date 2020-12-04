import env
import os

def getFolders(path):
    return next(os.walk(path))[1]

def fillEntriesArray(filePath, array):
    f = open("static/addedWebsites.js", "w")

    f.write("addedWebsites=[")
    for website in array:
        websiteArrString = '"{0}",'.format(website)
        f.write(websiteArrString)
    f.write("]")
    f.close()   