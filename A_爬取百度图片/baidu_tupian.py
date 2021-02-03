"""
@author: wanghongliang
@file: baidu_tupian.py
@time: 2021/1/26 14:45 
"""
import requests, re, os
from lxml import html

etree = html.etree

# s = requests.Session()
# s.keep_alive = False

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              "Host":"tupian.baidu.com","Referer":"http://tupian.baidu.com/"}
url = "http://tupian.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=car"
# url_zh = "http://tupian.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1611648671713_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=车子"
dirpath = os.path.join(os.getcwd() , "image")

res = requests.get(url, headers=header, allow_redirects=False)
# html = etree.HTML(res.text, etree.HTMLParser())
# result = html.xpath("//div[@id='imgid']")
# print(result)
result = re.findall(r'"objURL":"(.*?)"', res.text)
print(len(result))
for line in result:
    print(line)


if not os.path.isdir(dirpath):
    os.mkdir(dirpath)

index = 1
for line in result:
    print(str(index) + ": Downloading:", line)
    try:
        res_image = requests.get(line, timeout=5)
        if str(res_image.status_code)[0] == "4":
            print("4xx， 未下载成功：", line)
            index += 1
            continue
        filename = os.path.join(dirpath, str(index) + ".jpg")
        with open(filename, 'wb') as f:
            f.write(res_image.content)
        index += 1
    except Exception as e:
        print("下载出错，未下载成功：", line, e)


# print(res.text)



