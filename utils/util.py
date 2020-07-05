"""
@author: wanghongliang
@file: util.py
@time: 2020/7/2 19:29 
"""
import requests
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8"}


def get_page(url):
    try:
        res = requests.get(url, headers=header)
        # res.encoding = "GB2312"
        res.encoding = res.apparent_encoding
        # print(res.apparent_encoding)
        # print(res.text)
        return res.text
    except Exception as e:
        print("获取页面出错， error: ", e)
        return None

# start_url = "http://www.66ip.cn/{}.html"
# urls = [start_url.format(page) for page in range(1, 4 +1)  ]
# for i in urls:
#     print(34343)
#     print(i)
#     get_page(i)

# get_page("http://www.66ip.cn/1.html")
