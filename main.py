#! /opt/homebrew/bin/python3

from bs4 import BeautifulSoup
import requests

def isParenthesized(a_tag):
    parent_text = a_tag.parent.get_text(strip=True)
    link_index = parent_text.find(a_tag.get_text(strip=True))     

    if link_index != -1:
        text_before = parent_text[:link_index]
        text_after = parent_text[link_index + len(a_tag.get_text(strip=True)):]

        if '(' in text_before and ')' in text_after:
            return True

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
    
# print(hit("/wiki/Philosophy"))

def scrape(target):
    link = hit(target)
    print(link)
    scrape(link)

# scrape("/wiki/Special:Random")
scrape("/wiki/Philosophy")