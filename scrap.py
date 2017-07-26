#!/usr/bin/env python3
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup


def getTtitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.html.h1
    except AttributeError as e:
        return None
    return title
title = getTtitle("http://www.pythonscraping.com/pages/page1.html")

if title:
    print(title)
else:
    print("Title could not be found")
