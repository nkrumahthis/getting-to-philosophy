# from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/Special:Random')

print(r.content)
