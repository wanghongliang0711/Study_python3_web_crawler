"""
@author: wanghongliang
@file: RedisClient.py
@time: 2020/6/28 14:15 
"""
import redis
from random import choice


MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'


class RedisClient(object):

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        redis 取出的结果默认是字节，我们可以设定 decode_responses=True 改成字符串。
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理， 分数是 10 ？？
        :return:
        """
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, {proxy: score})

    def random_proxy(self):
        """
        随机获取有效代理，首先最高分，其次其他分
        :return:
        """
        # 获取 100 分的代理名
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):  # 这里有问题，是从0~100中随机选的
                return choice(result)
            else:
                raise Exception("没有找到可用代理！！")

    def decrease(self, proxy):
        """
        代理值减 1 ， 如果小于最小值， 则删除
        :param proxy:
        :return:
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, "当前分数", score, "减一")
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            print('代理', proxy, '当前分数', '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        :param proxy:
        :return:
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理 设置为最大值
        :param proxy:
        :return:
        """
        print("代理", proxy, "可用， 设置为", MAX_SCORE)
        return self.db.zadd(REDIS_KEY, {proxy: MAX_SCORE})

    def count(self):
        """
        获取数量
        :return:
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return:
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)


