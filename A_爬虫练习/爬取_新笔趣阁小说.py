"""
@author: blake.wang
@file: 爬取_搜读小说.py
@time: 2021/11/25 14:01 
"""
import time

import requests
from lxml import html


etree = html.etree


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
s = requests.Session()
s.keep_alive = False


def get_book_data(start_page, f):
    res = s.get(start_page, headers=header)
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.text, etree.HTMLParser())
    title = html.xpath('//div[@id="wrapper"]//div[@class="bookname"]//h1//text()')
    title_str = str(title[0]).replace(" ", "").replace("\n", "") + "\n"
    print(title_str)
    f.write(title_str)
    article_content = html.xpath('//div[@id="wrapper"]//div[@id="content"]//text()')
    for content_detail in article_content:
        # print(content_detail)
        content_detail_str = str(content_detail).replace(" ", "").replace("\ue1bc","").replace("\xa0","").replace("\n","").replace("\r","") + "\n"
        if content_detail_str != "\n":
            f.write(content_detail_str)
        # print(content_detail_str)
    next_content = html.xpath('//div[@class="bottem1"]/a/@href')[-2]
    next_content_url = "https://www.xbiquge.la"+next_content
    if next_content_url.endswith(".html"):
        print(next_content_url)
        time.sleep(1)  # 怕被拒绝访问，加等待时间
        get_book_data(next_content_url, f)
    else:
        f.close()
        print("结束...")


file_name = "星门" + ".txt"


def main():
    f = None
    try:
        # 从第几章开始
        # https://www.xbiquge.la/25/25858/36605399.html # 夜的命名术
        # https://www.xbiquge.la/84/84419/35682318.html # 星门
        start_page = "https://www.xbiquge.la/84/84419/35682318.html"
        f = open(file_name, 'w', encoding='utf-8')
        get_book_data(start_page, f)
    except Exception as e:
        print("main error . message: ", e)
    finally:
        if f is not None:
            f.close()


if __name__ == '__main__':
    main()
