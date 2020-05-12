"""
@author: wanghongliang
@file: 04_study_BeautifulSoup.py
@time: 2020/5/11 14:23 
"""

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body name="123">
<p class="title" name="dromouse"><b>The Dormouse's story</b>
<b>The Dormouse's story1<a>链接</a></b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
markup="<b><!--Hey, buddy. Want to buy a used parser?--></b>"

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.head)    # 获取head标签
print(type(soup.head))
print(soup.p.b)     # 获取p节点下的b节点
print(type(soup.p.b))
print(soup.a.string)    # 获取a标签下的文本，只获取第一个
print(type(soup.a.string))

"""name属性获取节点名称："""
print("name属性获取节点名称：", soup.body.name)


""" attrs属性获取节点属性，也可以字典的形式直接获取，
返回的结果可能是列表或字符串类型，取决于节点类型"""
print("attrs属性获取节点属性：", soup.p.attrs)
print("attrs属性获取节点属性：", soup.p.attrs['class'])
# 更简单的获取方式：
print("attrs属性获取节点属性：", soup.p['name'])
print("attrs属性获取节点属性：", soup.p['class'])


""" string属性获取节点元素包含的文本内容： """
print("string属性获取节点元素包含的文本内容：", soup.p.string)


""" contents属性获取节点的直接子节点，以列表的形式返回内容 """
print("contents属性获取节点的直接子节点：", soup.p.contents)

""" children属性获取的也是节点的直接子节点，只是以生成器的类型返回 """
print("children属性获取的也是节点的直接子节点：", soup.p.children)
for i, chil in enumerate(soup.p.children):
    print(i, chil)

""" descendants属性获取子孙节点，返回生成器 """
print("descendants属性获取子孙节点：", soup.p.descendants)
for i, chil in enumerate(soup.p.descendants):
    print(i, chil)


""" parent属性获取父节点，parents获取祖先节点，返回生成器 """
print("parent属性获取父节点:",soup.a.parent)
print("parents获取祖先节点，返回生成器: ", list(enumerate(soup.p.parents)))


""" next_sibling属性返回下一个兄弟节点
previous_sibling返回上一个兄弟节点,注意换行符也是一个节点
next_siblings和previous_siblings分别返回前面和后面的所有兄弟节点，返回生成器
"""
print("next_sibling属性返回下一个兄弟节点:", soup.p.next_sibling)
print("previous_sibling返回上一个兄弟节点:", soup.p.previous_sibling)
print("next_siblings属性返回下一个兄弟节点:", list(enumerate(soup.p.next_siblings)))
print("previous_siblings返回上一个兄弟节点:", list(enumerate(soup.p.previous_siblings)))


"""
next_element和previous_element属性获取下一个被解析的对象，或者上一个
next_elements和previous_elements迭代器向前或者后访问文档解析内容
"""
print("next_element获取下一个被解析的对象:", soup.p.next_element)
print("previous_element获取上一个被解析的对象:", soup.p.previous_element)
print("next_elements获取下一个被解析的对象:", list(enumerate(soup.p.next_elements)))
print("previous_elements获取上一个被解析的对象:", list(enumerate(soup.p.previous_elements)))


print("----------------")
print(soup.html.body['name'])
