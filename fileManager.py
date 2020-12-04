import env


def getWebsitesInEnv():
    return localWebsiteDirs

def fillEntriesArray(filePath, array):
    f = open("static/addedWebsites.js", "w")

    f.write("addedWebsites=[")
    for website in localWebsiteDirs:
        websiteArrString = '"{0}",'.format(website)
        f.write(websiteArrString)
    f.write("]")
    f.close()   