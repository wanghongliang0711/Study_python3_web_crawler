"""
@author: wanghongliang
@file: 04_study_BeautifulSoup.py
@time: 2020/5/11 14:23 
"""

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    ddd
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">王 Tillie 量</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<span>中文</span>"""

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.select('title'))  # tag
print(soup.select('p a'))   # 通过tag标签逐层查找
print(soup.select('body > span'))   # 查找某个tag标签下的直接子标签

print(type(soup.select('body > span')[0]))  # bs4.element.Tag

print(soup.select('#link1 ~ .sister'))  # 查找兄弟节点标签：

print(soup.select('.title'))  # 通过CSS类名查找
print(soup.select('[class~=title]'))  # 通过CSS类名查找


print(soup.select('#link1'))  # 通过tag的id查找
print(soup.select('a#link2'))  # 通过tag的id查找


print(soup.select('a[href]'))  # 通过是否存在某个属性来查找


print(soup.select('a[href="http://example.com/elsie"]'))  # 通过属性的值来查找匹配
# 匹配值的开头
print(soup.select('a[href^="http://example.com/"]'))  # 通过属性的值来查找匹配
# 匹配值的结尾
print(soup.select('a[href$="tillie"]'))
# 模糊匹配
print(soup.select('a[href*=".com/el"]'))


"""
获取属性、获取文本方法都一样
"""

"""
（4）tag修改方法
"""
markup='<a href="http://www.baidu.com/">baidu</a>'
soup=BeautifulSoup(markup,'lxml')
soup.a.string='百度'
print(soup.a)

"""
Tag.append()  就好像Python的列表的 .append() 方法
"""

soup.a.append('一下')

print(soup.a)

"""
new_tag()方法用于创建一个tag标签
insert()将元素插入到指定的位置
inert_before()在当前tag或文本节点前插入内容
insert_after()在当前tag或文本节点后插入内容
clear()移除当前tag的内容
extract()将当前tag移除文档数，并作为方法结果返回
prettify()将Beautiful Soup的文档数格式化后以Unicode编码输出，tag节点也可以调用
get_text()输出tag中包含的文本内容，包括子孙tag中的内容
soup.original_encoding 属性记录了自动识别的编码结果
from_encoding:参数在创建BeautifulSoup对象是可以用来指定编码，减少猜测编码的运行速度
#解析部分文档，可以使用SoupStrainer类来创建一个内容过滤器，它接受同搜索方法相同的参数
"""

