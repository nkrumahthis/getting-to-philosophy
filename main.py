from bs4 import BeautifulSoup
import requests

def isInteresting(link):
    # print(link)
    # print(link.parent.name)
    if(("role" in link.parent.attrs) and ("note" in link.parent.attrs["role"])):
        return False
    if("class" in link.attrs):
        return False
    # if(link.parent.name == "figcaption"):
    #     return False
    # if(link.parent.name != "p" and link.parent.name != "b"):
    #     return False
    return True


r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
# r = requests.get('https://en.wikipedia.org/wiki/Lutz_Sch%C3%BClbe')

soup = BeautifulSoup(r.content, 'html.parser')

artTitle = soup.title.text

print(artTitle)

# get first link
# contentLinks = soup.body.find("div", id="mw-content-text").find_all("a")
# links = []

allp = soup.body.find("div", id="mw-content-text").find_all("p")

# print(allp)

thep = []

for p in allp:
    if("class" in p.attrs and "mw-empty-elt" in p.attrs["class"]):
        continue
    thep.append(p)

print(thep[0].a)

# contentLinks = soup.body.find("div", id="mw-content-text").p.find_all("p")

# print(soup.body.find("div", id="mw-content-text"))
# links = []

# for link in contentLinks:
#     # print(link)
#     if(isInteresting(link)):
#         links.append(link)

# if(len(links) == 0):
#     print("No links found")
# else:
#     print(links[0])