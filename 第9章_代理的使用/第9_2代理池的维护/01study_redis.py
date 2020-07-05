"""
@author: wanghongliang
@file: 01study_redis.py
@time: 2020/6/28 14:56 
"""
import redis

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

r.zadd("zset1", {'m1':14,'m2':8,'m3':100})
r.zadd("zset2", {'n1':14,'n2':15})
print(r.zcard("zset1")) # 集合长度
print(r.zcard("zset2")) # 集合长度
print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数

print(r.zscore("zset1", "m15"))
print(r.zscore("zset1", "m1"))
print("r.zrangebyscore", r.zrangebyscore("zset1", 10, 50))
print(r.zrangebyscore("zset1", 50, 100))

print(r.zrevrange("zset1", 0, 100))

print(r.zincrby("zset1", -1, "m3"))
print(r.zrange("zset1", 0, -1, withscores=True))
print(r.zrem("zset1", "m1"))
print(r.zrange("zset1", 0, -1, withscores=True))


