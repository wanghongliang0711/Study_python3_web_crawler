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

"""
find_all(name,attrs,recursive,text,**kwargs)：
name 是 标签(tag)
attrs  传入的属性
text参数用来匹配节点的文本,传入的形式可以是字符串也可以是正则表达式对象
recursive表示，如果只想搜索直接子节点可以将参数设为false：recursive=Flase
查询所有符合条件的元素，其中的参数"""

print(soup.find_all(name='p'))  #标签查找
print(type(soup.find_all(name='p')[0]))

print(soup.find_all("a", id='link1')) # 标签 + 属性
print(soup.find_all('a', attrs={'class':'sister','id':'link3'})) # 标签 + 多属性

print(soup.find_all('p', class_='title'))   # class特殊性,此次传入的参数是**kwargs

print(soup.find_all(text=re.compile('Tillie')))  # 文本过滤
print(soup.find_all(text='王 Tillie 量'))  # 文本过滤
print(soup.find_all('a',limit=2))  #限制输出数量

for p in soup.find_all(name='p'):
    print("第一层", p)
    for a in p.find_all(name='a'):
        print(a.string)


"""
find( name , attrs , recursive , text , **kwargs )：它返回的是单个元素，也就是第一个匹配的元素，类型依然是tag类型

参数同find_all()一样

另外还有许多查询方法，其用法和前面介绍的find_all()方法完全相同，只不过查询范围不同，参数也一样

find_parents(name , attrs , recursive , text , **kwargs )和
find_parent(name , attrs , recursive , text , **kwargs )：
前者返回所有祖先节点，后者返回直接父节点

find_next_siblings(name , attrs , recursive , text , **kwargs )和
find_next_sibling(name , attrs , recursive , text , **kwargs )：
对当前tag后面的节点进行迭代，前者返回后面的所有兄弟节点，后者返回后面第一个兄弟节点

find_previous_siblings(name , attrs , recursive , text , **kwargs )和
find_previous_sibling(name , attrs , recursive , text , **kwargs )：
对当前tag前面的节点进行迭代，前者返回前面的所有兄弟节点，后者返回前面的第一个兄弟节点

find_all_next(name , attrs , recursive , text , **kwargs )和
find_next(name , attrs , recursive , text , **kwargs )：
当前tag之后的tag和字符串进行迭代，前者返回所有符合条件的节点，后者返回第一个符合条件的节点

find_all_previous()和find_previous()：
对当前tag之前的tag和字符串进行迭代，前者返回节点后所有符合条件的节点，
后者返回第一个符合条件的节点

"""

