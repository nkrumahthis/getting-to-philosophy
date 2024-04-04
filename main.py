from bs4 import BeautifulSoup
import requests

def isInteresting(link):
    # print(link)
    if(("role" in link.parent.attrs) and ("note" in link.parent.attrs["role"])):
        return False
    if("class" in link.attrs):
        return False
    if(link.parent.name == "figcaption"):
        return False
    if(link.parent.name != "p"):
        return False
    return True


r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
soup = BeautifulSoup(r.content, 'html.parser')

artTitle = soup.title.text

print(artTitle)

# get first link
contentLinks = soup.body.find("div", id="mw-content-text").find_all("a")
links = []

for link in contentLinks:
    if(isInteresting(link)):
        links.append(link)

print(links[0])