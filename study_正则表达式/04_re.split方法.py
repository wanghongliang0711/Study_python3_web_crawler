"""
@author: wanghongliang
@file: 04_re.split方法.py
@time: 2020/5/10 11:05 
"""
"""
split 方法按照能够匹配的子串将字符串分割后返回列表
"""

import re

print(re.split('\W+', 'runoob, runoob22, runoob44.'))

# 分割次数
print(re.split('\W+', 'runoob, runoob22, runoob44.', 1))


