#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

print(bsObj.find("img", {"src": "../img/gifts/img2.jpg"}).parent.previous_sibling.get_text())

for sibling in bsObj.find("table", {"id": "giftList"}):
    print(sibling.get_text())
