"""
@author: wanghongliang
@file: requests_post.py
@time: 2021/7/19 18:41 
"""
import requests,json

data = {'test':'wang_ets', 'age':'25'}
data1 = {'test1':'wang_ets', 'age1':'25'}
# r = requests.get("http://127.0.0.1:5000/get_args", params=data)

s = json.dumps({'key1': 'value1', 'key2': 'value2'})

# r = requests.post("http://127.0.0.1:5000/post_args", data=data)
# r = requests.post("http://127.0.0.1:5000/post_args_json", data=data)  # request.form
# r = requests.post("http://127.0.0.1:5000/post_args_json", json=data)  # request.data request.json
# r = requests.post("http://127.0.0.1:5000/post_args_json", params=data)  # request.args
r = requests.post("http://127.0.0.1:5000/post_args_json", data1)  # request.form


print(r.text)

