"""
@author: wanghongliang
@file: Crawler.py
@time: 2020/6/28 16:21 
"""
import json
import time

import aiohttp
# from .utils.util import get_page
from utils.util import get_page
from lxml import etree
from lxml.html import fromstring

class Crawler(object):
    def get_proxies(self):
        proxies = []
        for i1 in self.crawl_daili66():
            print("成功获取代理： ", i1)
            proxies.append(i1)
        for i2 in self.crawl_proxyGoubanjia():
            print("成功获取代理： ", i2)
            proxies.append(i2)
        for i3 in self.crawl_kuaidaili():
            print("成功获取代理： ", i3)
            proxies.append(i3)
        return proxies


    def crawl_daili66(self, page_count=2000):
        """
        获取代理66
        :param page_count: 页码
        :return:
        """
        start_url = "http://www.66ip.cn/{}.html"
        urls = [start_url.format(page) for page in range(1, page_count +1)  ]
        for url in urls:
            print("Crawler : ", url)
            html = get_page(url)
            time.sleep(1)
            # print(html)
            if html:
                htmlEle = etree.HTML(html, etree.HTMLParser())
                result_ip = htmlEle.xpath("//div[@id='main']//table//tr[position()>1]/td[1]/text()")
                result_port = htmlEle.xpath("//div[@id='main']//table//tr[position()>1]/td[2]/text()")
                # result1 = html.xpath('//li[contains(@class,"aaa")]/a/text()')
                # print(result_ip)
                # print(result_port)
                for i in range(0, len(result_ip)):
                    # print(':'.join([result_ip[i], result_port[i]]))
                    yield ':'.join([result_ip[i], result_port[i]])

    def crawl_proxyGoubanjia(self):
        """
        获取代理 http://www.goubanjia.com/
        :return:
        """
        start_url = "http://www.goubanjia.com/"
        html = get_page(start_url)

        # root = etree.strip_elements()
        # print(html)
        if html:
            htmlEle = etree.HTML(html, etree.HTMLParser())
            result = htmlEle.xpath("//td[@class='ip']")
            # print(result)
            # print(len(result))

            for td in result:
                # p = td.xpath(".//p[@style='display:none;']")
                # p1 = td.xpath(".//p[@style='display: none;']")
                etree.strip_elements(td, 'p')
                # print(etree.tostring(td))
                # print(len(p))
                # print(len(p1))

                text = td.xpath(".//text()")
                # print(text)
                # print(''.join(text))
                yield ''.join(text)


            # print("---"+result+"---")


    def crawl_kuaidaili(self, page_count=3000):
        """
        https://www.kuaidaili.com/free/inha/1/
        :param page_count:
        :return:
        """
        start_url = "https://www.kuaidaili.com/free/inha/{}/"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            import time
            time.sleep(2)
            print("Crawler : ", url)
            html = get_page(url)
            if html:
                htmlEle = etree.HTML(html, etree.HTMLParser())
                result_ip = htmlEle.xpath("//div[@id='list']//table//tr/td[1]/text()")
                result_port = htmlEle.xpath("//div[@id='list']//table//tr/td[2]/text()")
                # print(result_ip)
                # print(result_port)
                for i in range(0, len(result_ip)):
                    # print(':'.join([result_ip[i], result_port[i]]))
                    yield ':'.join([result_ip[i], result_port[i]])




# d = Crawler()
# f = (d.get_proxies())
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))







