#! /opt/homebrew/bin/python3

from bs4 import BeautifulSoup
import requests

def isParenthesized(a_tag):
    if a_tag.previous_sibling and a_tag.next_sibling:
        if ('(' in a_tag.previous_sibling.string.strip()) and (')' in a_tag.next_sibling.string.strip()):
            return True
        else:
            return False
    else:
        return False
    
def isItalicized(a_tag):
    return a_tag.parent.name in ['i', 'em']

def hit(target):
    url = 'https://en.wikipedia.org' + target

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    print(soup.title.text.split("-")[0].strip())

    main_content = soup.body.find(attrs={'class': 'mw-parser-output'})

    for element in main_content.select(".infobox"):
      element.decompose()

    links = main_content.find_all("a")

    interestingLinks = []

    for a in links:
        if isItalicized(a):
            continue
        if isParenthesized(a):
            continue
        if (a.parent.name in ["p", "li"]):
            # print(a.parent)
            interestingLinks.append(a)

    if(len(interestingLinks) > 0):
       return interestingLinks[0]
    else:
       return None

link = hit("/wiki/SET_Saxmundham_School")
# link = hit("/wiki/Special:Random")
print(link)