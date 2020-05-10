"""
@author: wanghongliang
@file: 03_re.findall方法.py
@time: 2020/5/10 10:52 
"""

"""在字符串中找到正则表达式所匹配的所有子串，
并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

"""

import re

result = re.findall(r"\d+", "run88oob123google456")
print(result)


result = re.findall(r"\d+", "run88oob123google456")
print(result)

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

str2 = "4 4"
print(str2.split(" "))
