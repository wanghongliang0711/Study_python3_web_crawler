"""
@author: wanghongliang
@file: 02_study_lxml_文件解析.py
@time: 2020/5/11 9:18 
"""
from lxml import etree

html = etree.parse("002文本格式化.html", etree.HTMLParser()) # 指定解析器HTMLParser会根据文件修复HTML文件中缺失

result = etree.tostring(html,encoding='utf-8')

# result=etree.tostringlist(html)  # 解析成列表

print(type(html))
print(type(result))
print(result.decode('utf-8'))
