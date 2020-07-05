"""
@author: wanghongliang
@file: test.py
@time: 2020/5/14 17:03 
"""
import json

# json 的数据要使用双引号，否则报错
js = """[{"wang":"引号","wang1":"引号"},{"wang":"123"}]"""

print(type(js))

data = json.loads(js)
print(data)
print(type(data))

# print(data[0]["wang2"])  # 报错
print(data[0].get('wang2')) # None
print(data[0].get('wang2', "error"))  # error

data = {"id":"12345", "name":"wang", "age":20}

keys = ','.join(data.keys())
# keys1 = ','.join(['id', 'name', 'age'])

values = ','.join(['%s'] * len(data))

sql = f"insert ({keys}) values ({values})"

print(sql)
picture_url = "https://i3.mmzztt.com/2014/07/20140711w802.jpg"

picture_name = picture_url.split("/")[-1]
print(picture_name)


for i in range(1, 1000, 10):
    print(i)

