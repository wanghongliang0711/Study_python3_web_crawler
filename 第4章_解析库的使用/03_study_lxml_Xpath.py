"""
@author: wanghongliang
@file: 03_study_lxml_Xpath.py
@time: 2020/5/11 10:28 
"""

from lxml import etree

html = etree.parse("002文本格式化.html", etree.HTMLParser())

result = html.xpath('//*')

print(result)

print(html.xpath('//b'))


text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

""" 获取父节点 """
html = etree.HTML(text, etree.HTMLParser())
result=html.xpath('//a[@href="link2.html"]/../../li/@class')
result1=html.xpath('//a[@href="link2.html"]/parent::*/@class')
print(result)
print(result1)


""" 属性匹配 """
html1 = etree.HTML(text, etree.HTMLParser())
result = html1.xpath("//li[@class='item-1']")
print(result)

""" 文本获取 """
html = etree.HTML(text, etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()') #获取a节点下的内容
result1 = html.xpath('//li//text()')
print(result)
print(result1)

"""  属性获取  """
result = html.xpath('//li/a/@href')
print(result)

"""  属性多值匹配  """
text1='''
<div>
    <ul>
         <li class="aaa item-0" name="item"><a href="link1.html">第一个</a></li>
         <li class="bbb item-1" name="fore"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''
html = etree.HTML(text1, etree.HTMLParser())
result = html.xpath('//li[@class="aaa"]/a/text()')
result1 = html.xpath('//li[contains(@class,"aaa")]/a/text()')
print(result)   # []
print(result1)  # ['第一个']

"""  多属性匹配  """
result = html.xpath('//li[contains(@class,"aa") and @name="item"]/a/text()')
print(result)


""" 按序选择 """
text1='''
<div>
    <ul>
         <li class="aaa" name="item"><a class="aaa" href="link1.html">第一个</a></li>
         <li class="aaa2" name="item"><a class="aaa2" href="link1.html">第二个</a></li>
         <li class="aaa3" name="item"><a class="aaa3" href="link1.html">第三个</a></li>
         <li class="aaa4" name="item"><a class="aaa4" href="link1.html">第四个</a></li> 
     </ul>
 </div>
'''
html = etree.HTML(text1,etree.HTMLParser())
result = html.xpath("//li/a/text()")   #获取所有li节点下a节点的内容
result1 = html.xpath("//li[1]/a/text()")  #获取第一个
result2 = html.xpath("//li[last()]/a/text()")  #获取最后一个
# position() 返回当前正在被处理的节点的 index 位置。
result3=html.xpath('//li[position()>2 and position()<4][contains(@class,"aaa")]/a/text()') # ['第三个']
result4=html.xpath('//li[last()-2][contains(@class,"aaa")]/a/text()') #获取倒数第三个
print(result)
print(result1)
print(result2)
print(result3)
print("result4 ", result4)


"""  节点轴选择  """
result = html.xpath('//li[1]/ancestor::*')  #获取所有祖先节点
result1 = html.xpath('//li[1]/ancestor::div')  #获取div祖先节点
result2=html.xpath('//li[1]/attribute::*')  #获取所有属性值
result3=html.xpath('//li[1]/child::*')  #获取所有直接子节点
result4=html.xpath('//ul/descendant::a')  #获取所有子孙节点的a节点
result5=html.xpath('//li[1]/following::*/@class')  #获取当前子节之后的所有节点
result6=html.xpath('//li[1]/following-sibling::*//text()')  #获取当前节点的所有同级节点

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)




# from lxml.html import etree
from lxml.html import fromstring, HtmlElement

test_html = '''<p><span>hello</span><span>world</span></p>'''
test_element = fromstring(test_html)
# etree.strip_tags(test_element,'span') # 清除span标签
# print(etree.tostring(test_element))


etree.strip_elements(test_element,'span') # 清除span标签
print(etree.tostring(test_element))



