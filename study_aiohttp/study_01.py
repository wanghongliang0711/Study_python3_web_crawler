"""
@author: wanghongliang
@file: study_01.py
@time: 2020/6/30 19:28 
"""

from datetime import datetime

import requests
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.121 Safari/537.36"}


def get_movie_url():
    req_url = "https://movie.douban.com/chart"
    response = requests.get(url=req_url, headers=headers)
    html = etree.HTML(response.text)
    movies_url = html.xpath(
        "//*[@id='content']/div/div[1]/div/div/table/tr/td/a/@href")
    return movies_url


def get_movie_content(movie_url):
    response = requests.get(movie_url, headers=headers)
    result = etree.HTML(response.text)
    movie = dict()
    name = result.xpath('//*[@id="content"]/h1/span[1]//text()')
    author = result.xpath('//*[@id="info"]/span[1]/span[2]//text()')
    movie["name"] = name
    movie["author"] = author
    return movie


if __name__ == '__main__':
    start = datetime.now()
    movie_url_list = get_movie_url()
    movies = dict()
    for url in movie_url_list:
        print(url)
        movies[url] = get_movie_content(url)
    print(movies)
    print("同步用时为：{}".format(datetime.now() - start))