"""
@author: wanghongliang
@file: test1.py
@time: 2021/1/26 15:49 
"""
import re
import itertools

line = 'ata":[{"thumbURL":"http://img5.imgtn.bdimg.com/it/u=2177545615,4060911584&fm=26&gp=0.jpg","replaceU'

result = re.findall(r'"thumbURL":"(.*)",', line)

ss = "http://n.sinaimg.cn/sinacn/w640h435/20180207/520a-fyrhcqz3996992.jpg"

print(ss.split("/")[-1].split(".")[0])

def buildDum():
    list1 = (itertools.count(start=0, step=30))
    return list1

# sss = buildDum()
# for i in sss:
#     print(i)

import urllib.parse

word = urllib.parse.quote("word王")
print(word)


se = []
sd = [1,23,5]
se = se + sd
# se.append(sd)
print(se)
se.reverse()
print(se)
t = 0
while True:
    if t==5:
        break
    t += 1
    print(t)

import you_get

from you_get.extractor import VideoExtractor

# VideoExtractor.download_by_url()
#
# VideoExtractor.download()

from you_get import common
import you_get

you_get.common.download_urls()

import sys

list1 = ["http://v.qq.com/x/page/p0342w3cwn2.html",
         "http://www.bilibili.com/video/av92868892",
         "http://my.tv.sohu.com/us/324175385/94969125.shtml"]

directory = r'D:\test'
for url in list1:
    print(url)
    # url = 'https://www.bilibili.com/video/BV1me411W7J5'
    # sys.argv = ['you-get', '-o', directory, "-O", "1", url]
    sys.argv = ['you-get', '-o', directory, url]
    common.main()





