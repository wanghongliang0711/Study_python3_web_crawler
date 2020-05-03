"""
@author: wanghongliang
@file: requests_get.py
@time: 2020/5/3 15:22 
"""
import requests

# requests请参考下面链接
#  git@github.com:wanghongliang0711/python-requests-study.git


r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)


print("-------------------------------------")

r = requests.get("http://httpbin.org/get")
print(r.text)

data = {'name':'wang', 'age':'25'}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)
