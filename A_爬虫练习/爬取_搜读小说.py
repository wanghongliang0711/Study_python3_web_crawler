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

file_name = "朕" + ".txt"


def get_book_data(start_page, f):
    res = s.get(start_page, headers=header)
    html = etree.HTML(res.text, etree.HTMLParser())
    title = html.xpath('//div[@class="nr_title"]//h3//text()')
    title_str = str(title[0]).replace(" ", "").replace("\n", "") + "\n"
    print(title_str)
    f.write(title_str)
    article_content = html.xpath('//div[@id="articlecontent"]//p[@class="content_detail"]//text()')
    for content_detail in article_content:
        content_detail_str = str(content_detail).replace(" ", "").replace("\xa0","").replace("\n","") + "\n"
        f.write(content_detail_str)
        # print(content_detail_str)

    next_content = html.xpath('//div[@class="nr_page"]/a/@href')[-1]
    next_content_url = "http://www.soduso.cc"+next_content
    if next_content_url.endswith(".html"):
        print(next_content_url)
        time.sleep(1)  # 怕被拒绝访问，加等待时间
        get_book_data(next_content_url, f)
    else:
        f.close()
        print("结束...")


def main():
    f = None
    try:
        # http://www.soduso.cc/novel/67837/read_35923837.html
        # 从第几章开始
        start_page = "http://www.soduso.cc/novel/67837/read_35923837.html"
        f = open(file_name, 'w')
        get_book_data(start_page, f)
    except Exception as e:
        print("main error . message: ", e)
    finally:
        if f is not None:
            f.close()


if __name__ == '__main__':
    main()
