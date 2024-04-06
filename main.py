#! /opt/homebrew/bin/python3

from bs4 import BeautifulSoup
import requests

def isParenthesized(a_tag):
    if (a_tag.previous_sibling is not None) and (a_tag.next_sibling is not None):
        if ('(' in a_tag.previous_sibling.string.strip()) and (')' in a_tag.next_sibling.string.strip()):
            return True
        else:
            return False
    else:
        return False

def isItalicized(a_tag):
    if(a_tag.parent != None):
        return a_tag.parent.name in ['i', 'em']
    return False

def isContent(a_tag):
    if(a_tag.parent != None):
        return (a_tag.parent.name in ["p", "li"])
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

    interestingLinks = []

    for a in links:
        if isItalicized(a):
            continue
        if isParenthesized(a):
            continue
        if isContent(a):
            # print(a.parent)
            interestingLinks.append(a)

    if(len(interestingLinks) > 0):
       print(interestingLinks[0])
       return interestingLinks[0].attrs["href"]
    else:
       return None

# link = hit("/wiki/George_Frederic_Augustus_I")
link = hit("/wiki/Special:Random")
print(link)

def test_hit():
    assert hit("/wiki/SET_Saxmundham_School") == "/wiki/Free_school_(England)"