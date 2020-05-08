# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 11:25
# @File    : 02_re.search方法.py
''' '''
import re

'''re.search 扫描
整个字符串并返回第一个成功的匹配。
re.search(pattern, string, flags=0)
'''

#  方法可以输出匹配的范围 span()
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())

line = "Cats are smarter than dogs"
# line = "55"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
print(searchObj)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("searchObj.groups() : ", searchObj.groups())
else:
    print("Nothing found!!")

"""
re.match与re.search的区别
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，
则匹配失败，函数返回 None，而 re.search 匹配整个字符串，
直到找到一个匹配。
"""
