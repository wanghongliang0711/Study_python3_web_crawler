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
"""
"."可以匹配除了换行符之外的任意字符
"*" 匹配0个或多个表达式
"""
"""贪婪与非贪婪"""

"""贪婪  .* """
content = "Hello 1234567 World_This is a Regex Demo"
resu1 = re.match('^He.*(\d+).*Demo$', content, re.M|re.I)
print(resu1)
print(resu1.groups())  # ('7',)

"""非贪婪  .*? 在末尾时可能匹配不到任何字符"""
resu2 = re.match('He.*?(\d+)(.*?)', content, re.M|re.I)
print(resu2)
print(resu2.groups())  # ('1234567',)

"""
修饰符
re.I      使匹配对大小写不敏感
re.L        做本地化识别（locale-aware）匹配
re.M       多行匹配，影响 ^ 和 $
re.S         使 . 匹配包括换行在内的所有字符
re.U        根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X        该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""