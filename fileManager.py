import env
import os

def getFolders(path):
    return next(os.walk(path))[1]

def fillDirInfoFile(filePath, array, dirPath):
    f = open(filePath, "w")

    f.write("entries=[")
    for website in array:
        websiteArrString = '"../{0}",'.format(website)
        f.write(websiteArrString)
    f.write("]")
    f.write("\ndirPath='{}'".format(dirPath))

    f.close()   