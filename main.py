#! /opt/homebrew/bin/python3

from bs4 import BeautifulSoup
import requests

def isParenthesized(a_tag):
    if (a_tag.previous_sibling is not None) and (a_tag.next_sibling is not None):
        if (a_tag.previous_sibling.string is None):
            return False
        elif a_tag.next_sibling.string is None:
            return False
        if '(' == a_tag.previous_sibling.string.strip() or ')' == a_tag.next_sibling.string.strip():
            return True
        if '(' in a_tag.previous_sibling.string.strip():
            return True
        else:
            return False
    else:
        return False

def isItalicized(a_tag):
    if(a_tag.parent != None):
        if a_tag.parent.name in ['i', 'em']:
            return True
        elif "role" in a_tag.parent.attrs and a_tag.parent.attrs["role"] == "note":
            return True
    return False

def isContent(a_tag):
    if(a_tag.parent != None):
        return a_tag.parent.name == "p"
    return False

def isSelfLink(a_tag):
    if a_tag.attrs is not None and "class" in a_tag.attrs and "selflink" in a_tag.attrs["class"]:
        return True
    return False

def hit(target):
    url = 'https://en.wikipedia.org' + target

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    print(soup.title.text.split("-")[0].strip())

    main_content = soup.body.find(attrs={'class': 'mw-body-content'}).find(attrs={'class': 'mw-parser-output'})

    links = main_content.find_all("a")

    for element in main_content.select(".infobox"):
        element.decompose()

    for element in main_content.select(".sidebar"):
        element.decompose()
    
    interestingLinks = []

    for a in links:
        if isItalicized(a):
            continue
        if isParenthesized(a):
            continue
        if isSelfLink(a):
            continue
        if not isContent(a):
            continue
        if not "href" in a.attrs:
            continue
        interestingLinks.append(a)

    if(len(interestingLinks) > 0):
    #    print(interestingLinks[0].parent)
       return interestingLinks[0].attrs["href"]
    else:
       return None
    
# link = hit("/wiki/Geography")
# print(link)

def scrape(target):
    link = hit(target)
    print(link)
    scrape(link)

# scrape("/wiki/Special:Random")
scrape("/wiki/Geography")