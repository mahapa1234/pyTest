# encoding: utf-8

import requests
from requests import HTTPError
from bs4 import BeautifulSoup
import re
import os
#
# url = "http://w3.afulyu.pw/pw/thread.php?fid=15"
# url = 'http://w3.afulyu.pw/pw/htm_data/15/1803/1081464.html'
# url = 'http://w3.afulyu.pw/pw/thread.php?fid=15'
# url = 'http://p.usxpic.com/imghost/upload/image/20180330/33014501944.jpg'
# html = requests.get(url)
# dirPath = r'E:\hello\image\1.jpg'
# with open(dirPath, 'wb') as fp:
# 	fp.write(html.content)
urlHtml = 'http://w3.afulyu.pw/pw/thread.php?fid=15&page=1'
htmlHead = 'http://w3.afulyu.pw/pw/'
dirPath = 'E:\\hello\\image\\'


def get_html_bsObj(url):
    try:
        html = requests.get(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.content, "html.parser")
    except AttributeError as e:
        return None
    return bsObj


class GetDownLink(object):
    def __init__(self, url_image, typeIn='img'):
        self.url_image = url_image
        self.typeIn = typeIn
        self.name = ''

    def get_html_image(self):
        html = get_html_bsObj(self.url_image)
        return html

    def get_all_link(self):
        bsObj = self.get_html_image()
        res = bsObj.findAll(self.typeIn, {"src": re.compile(".+\.jpg")})
        return [i["src"] for i in res]


def downLink(listIn, dirPath):
    try:
        os.mkdir(dirPath)
    except Exception as e:
        print "mkdir error"
    for i in range(0, len(listIn)):
        fileName = '%s.jpg' % (i + 1)
        dirName = os.path.join(dirPath, fileName)
        image = requests.get(listIn[i])
        with open(dirName, 'wb') as fp:
            print "downing...... %s of %s" % (i + 1, len(listIn))
            fp.write(image.content)


# s1 = GetDownLink(url)
# list1 = s1.get_all_link()
# dirPath = 'E:\\hello\\image\\'
# downLink(list1, dirPath)


def get_html_list(urlHtml):
    bsObj = get_html_bsObj(urlHtml)
    res = bsObj.findAll('a', {"href": re.compile(
        "^htm_data.+.html"), "title": re.compile(".+")})
    res = [i['href'] for i in res]
    return res


def get_file_name(url):
    bsObj = get_html_bsObj(url)
    return re.search('\<title\>(.+\])\|.+', str(bsObj.title)).group(1)


def get_complete_image_html(listIn):
    # 获取全部的html页面的url
    global htmlHead
    listAll = get_html_list(listIn)
    return [os.path.join(htmlHead + i) for i in listAll]


def get_page_all_image(urlHtml):
    global dirPath
    list_Image_Html_Url = get_complete_image_html(urlHtml)
    for i in list_Image_Html_Url:
        fileName = get_file_name(i)
        dirName = os.path.join(dirPath, fileName)
        # print dirName
        s1 = GetDownLink(str(i))
        # print str(i),type(i)
        list1 = s1.get_all_link()
        # print list1
        downLink(list1, dirName)


get_page_all_image(urlHtml)
