"""
@author: wanghongliang
@file: study_01-2.py
@time: 2020/6/30 19:46 
"""

import asyncio
from datetime import datetime

import aiohttp
from lxml import etree
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.121 Safari/537.36"}


async def get_movie_url():
    req_url = "https://movie.douban.com/chart"
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=req_url, headers=headers) as response:
            result = await response.text()
            result = etree.HTML(result)
        return result.xpath("//*[@id='content']/div/div[1]/div/div/table/tr/td/a/@href")


async def get_movie_content(movie_url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=movie_url, headers=headers) as response:
            result = await response.text()
            result = etree.HTML(result)
        movie = dict()
        name = result.xpath('//*[@id="content"]/h1/span[1]//text()')
        author = result.xpath('//*[@id="info"]/span[1]/span[2]//text()')
        movie["name"] = name
        movie["author"] = author
    return movie

if __name__ == '__main__':
    start = datetime.now()
    loop = asyncio.get_event_loop()
    movie_url_list = loop.run_until_complete(get_movie_url())
    tasks = [get_movie_content(url) for url in movie_url_list]
    movies = loop.run_until_complete(asyncio.gather(*tasks))
    print(movies)
    print("异步用时为：{}".format(datetime.now() - start))