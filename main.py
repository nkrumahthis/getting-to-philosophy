from bs4 import BeautifulSoup
import requests

def has_unclosed_parenthesis(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return True  # There is a closing parenthesis without a corresponding opening one
            stack.pop()

    return len(stack) > 0  # If there are remaining opening parentheses in the stack, it means they are unclosed

def isParenthesized(a_tag):
    parent_text = a_tag.parent.get_text(strip=True)
    link_index = parent_text.find(a_tag.get_text(strip=True))     

    if link_index != -1:
        text_before = parent_text[:link_index]

        if has_unclosed_parenthesis(text_before):
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

def isRedLink(a_tag):
    if a_tag.attrs is not None and "class" in a_tag.attrs and "new" in a_tag.attrs["class"]:
        return True
    return False

def hit(target):
    url = 'https://en.wikipedia.org' + target

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    print("Exploring: " + soup.title.text.split("-")[0].strip())

    main_content = soup.body.find(attrs={'class': 'mw-body-content'}).find(attrs={'class': 'mw-parser-output'})

    for element in main_content.select(".infobox"):
        element.decompose()

    for element in main_content.select(".sidebar"):
        element.decompose()

    links = main_content.find_all("a")

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
        if isRedLink(a):
            continue
        interestingLinks.append(a)

    if(len(interestingLinks) > 0):
       return interestingLinks[0].attrs["href"]
    else:
       return None
    
