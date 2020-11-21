const websiteContainer = document.getElementById("websiteContainer")

for(website of addedWebsites){
    const websiteSpan = document.createElement("p")
    websiteSpan.innerHTML = website

    websiteContainer.appendChild(websiteSpan)
}