# encoding: utf-8

import requests
from requests import HTTPError
from bs4 import BeautifulSoup
import re


def getTile(url):
    try:
        html = requests.get(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.content, "html.parser")
    except AttributeError as e:
        return None
    return bsObj


def findImg(con='img', res=''):
    return res.findAll(con, {"src": re.compile(".+\.jpg")})


# url = "http://www.pythonscraping.com/pages/page3.html
# url = "http://w3.afulyu.pw/pw/thread.php?fid=15"
# url = 'http://w3.afulyu.pw/pw/htm_data/15/1803/1082541.html'
url = 'http://w3.afulyu.pw/pw/thread.php?fid=15'
# bsObj = getTile(url)
# if bsObj == None:
#     print "title could not be found"
# else:
#     res = findImg('img', bsObj)
#     for image in res:
#         print image["src"]

bsObj = getTile(url)
if bsObj == None:
    print "title could not be found"
else:
    res = bsObj.findAll('a', {"href": re.compile(
        "^htm_data.+.html"), "title": re.compile(".+")})
    # res = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
    res = [i['href'] for i in res]
    return res
    # print res
    # for i in res:
    # print i['title'].encode('utf-8')
    # print i.get_text().encode('utf-8')
