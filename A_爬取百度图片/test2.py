"""
@author: wanghongliang
@file: test2.py
@time: 2021/1/27 16:11 
"""
import platform, requests

print(platform.architecture())  #  系统架构 ('64bit', 'WindowsPE')


print(platform.system())   # Windows

print(platform.version())   # 系统版本 10.0.17763

print(platform.machine())   # CPU平台     AMD64

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              "authority":"search.bilibili.com"}

res = requests.get("https://search.bilibili.com/all?keyword=%E4%BA%A4%E9%80%9A%E6%A0%87%E5%BF%97&page=1", headers=header, timeout=10)

print(res)
print(res.text)

ss = "//www.bilibili.com/video/BV1YV411f7Zy?from=search"
print(ss[2:])
videoUrls = ["ee","rr","yy"]
for i in range(1, 10):
    if i == 3:
        break
    print(i)
    videoUrls = ["ee", "rr", "yy"]
    while True:
        if len(videoUrls) == 0:
            break
        url = videoUrls.pop()
        print(url)



