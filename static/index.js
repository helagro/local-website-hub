const dirNameViewer = document.getElementById("dirName")
const websiteContainer = document.getElementById("websiteContainer")

dirNameViewer.innerHTML = dirPath

for(website of entries){
    const websiteLink = document.createElement("a")
    websiteLink.innerHTML = website
    websiteLink.href = website

    websiteContainer.appendChild(websiteLink)
}