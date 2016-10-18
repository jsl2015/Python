# coding=utf-8
import urllib
import re


# add one line.
def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def get_img(img):
    reg = r'src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre, img)
    print imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

a = gethtml("http://desk.zol.com.cn/bizhi/6391_78665_2.html")
print get_img(a)
print a 







