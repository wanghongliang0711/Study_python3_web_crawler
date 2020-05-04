"""
@author: wanghongliang
@file: 01_re_match函数.py
@time: 2020/5/3 19:12 
"""


"""在线正则表达式
https://tool.oschina.net/regex/
"""
"""
re.match 尝试从字符串的起始位置匹配一个模式，
如果不是起始位置匹配成功的话，match()就返回none。
"""

import re

content = "Hello 1234567 World_This is a Regex Demo"
print(len(content))

result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())  # 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
print(result.groups())  # 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
print(result.group(1))
print(result.span())  # 方法可以输出匹配的范围 (0, 19)


"""贪婪与非贪婪"""






