"""
@author: wanghongliang
@file: 04_study_BeautifulSoup.py
@time: 2020/5/11 14:23 
"""

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
markup="<b><!--Hey, buddy. Want to buy a used parser?--></b>"

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())  # 把要解析的字符串以标准的缩进格式输出

print(soup.title.string)





