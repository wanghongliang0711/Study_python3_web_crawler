"""
@author: wanghongliang
@file: baidu_video.py
@time: 2021/1/28 9:34 
"""
from baiduspider import BaiduSpider
from pprint import pprint


# 实例化BaiduSpider
spider = BaiduSpider()

# 搜索网页
# pprint(spider.search_web(query='Python'))

# pprint(spider.search_pic(query='person', pn=1))

pprint(spider.search_video(query='car', pn=1))

