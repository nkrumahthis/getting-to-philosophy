from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
# r = requests.get('https://en.wikipedia.org/wiki/Sultan_Haydar')
soup = BeautifulSoup(r.content, 'html.parser')

artTitle = soup.title.text

print(artTitle)

# get first link
contentLinks = soup.body.find("div", id="mw-content-text").find_all("a")
links = []

for link in contentLinks:
    if("class" in link.attrs):
        continue
    links.append(link)
print(links[0])