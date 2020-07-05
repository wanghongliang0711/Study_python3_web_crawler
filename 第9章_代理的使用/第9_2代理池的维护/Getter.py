"""
@author: wanghongliang
@file: Getter.py
@time: 2020/7/5 13:38 
"""

from 第9章_代理的使用.第9_2代理池的维护.RedisClient import RedisClient
from 第9章_代理的使用.第9_2代理池的维护.Crawler import Crawler

class Getter(object):
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到代理池限制
        :return:
        """
        if self.redis.count() >= 5000:
            return True
        else:
            return False

    def run(self):
        print("获取器开始执行")
        if not self.is_over_threshold():
            for proxy in self.crawler.get_proxies():
                self.redis.add(proxy)

d = Getter()
d.run()

