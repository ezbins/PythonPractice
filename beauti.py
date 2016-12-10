#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", class_="green")
for name in nameList:
    print(name.get_text())

allText = bsObj.findAll(id="text")
print(allText[0].get_text())
