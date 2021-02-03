"""
@author: wanghongliang
@file: 爬取_妹子图.py
@time: 2020/5/16 14:01 
"""
import time

import requests
from lxml import html

etree = html.etree


header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              "Host":"www.mzitu.com","Referer":"https://www.mzitu.com/"}
s = requests.Session()
s.keep_alive = False

img_headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              'Referer':'https://www.mzitu.com/',
             "Host":"i3.mmzztt.com"
}

# 获取首页全部链接
def get_home_page_picture_url(url):
    res = s.get(url, headers=header)
    html = etree.HTML(res.text, etree.HTMLParser())
    result = html.xpath("//ul[@id='pins']/li/a/@href")
    return result

# 获取分页链接
def get_fen_page_url(page_picture_url):
    all_page_url = []
    for i in page_picture_url:
        res = s.get(i, headers=header)
        html = etree.HTML(res.text, etree.HTMLParser())
        max_num = html.xpath('//div[@class="pagenavi"]//a[last()-1]//text()')
        int_max_num = int(max_num[0].strip())
        for page in range(1, int_max_num+1):
            all_page_url.append(i+"/"+str(page))
    return all_page_url


def get_picture(fen_url):
    for i,url in enumerate(fen_url):
        if i % 2 == 0:
            time.sleep(2)
            print(i)
        print(f"url: {url}")
        res = s.get(url, headers=header)
        html = etree.HTML(res.text, etree.HTMLParser())
        picture_url = html.xpath('//div[@class="main-image"]//img/@src')
        print(f"picture_url: {picture_url}")
        with open('img_url.txt', 'a') as f:
            f.write(picture_url[0] + '\n')
        picture_name = picture_url[0].split("/")[-1]

        r = s.get(picture_url[0], headers=img_headers)

        with open("picture/"+ picture_name, 'wb') as f:
            f.write(r.content)



def main():
    num = 0
    for page in range(1, 3):
        # 主页url
        page_picture_url = get_home_page_picture_url(f"https://www.mzitu.com/page/{page}/")
        # 分页url
        fen_url = get_fen_page_url(page_picture_url)
        # 下载 图片
        get_picture(fen_url)
        num += len(fen_url)
        print(f"已经下载{num}个图片")
    print("全部下载完成")


if __name__ == '__main__':
    main()
