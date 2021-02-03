# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 15:02
# @File    : bilibili_video_download_R01.py
import requests, os, itertools, threading, time
import urllib.parse
# 需要安装you_get  pip3 install you_get
import you_get
from lxml import html

glock = threading.Lock()
etree = html.etree
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              "authority":"search.bilibili.com"}

videoUrls = []

# 创建文件夹
def makeDir(dirpath):
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

# 生成网址列表
def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"https://search.bilibili.com/all?keyword={word}&page={pn}"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=1, step=1))
    return urls

def thread_download_video(result, dirpath):
    try:
        while True:
            global glock
            glock.acquire()
            print("本页还剩 ", len(result), " 个没有开始下载。")
            if len(result) == 0:
                glock.release()
                break
            one_url = result.pop()
            if one_url.startswith('//'):
                one_url = one_url[2:]
            glock.release()
            print("开始下载： ", one_url)
            zhiling = ('you-get -o "{path}" -l --no-caption --no-merge -a {url}'.format(path=dirpath, url=one_url))
            print(zhiling)
            success_result = os.system(zhiling)
            if success_result == 0:
                print(one_url, "下载成功。")
            else:
                print(one_url, "下载失败！！！")
    except Exception as e:
        print("thread_download_video 下载出错，未下载成功：", e)
        time.sleep(8)

def download_video(urls, dirpath):
    try:
        for url in urls:
            print(url)
            res = requests.get(url, headers=header, timeout=10)
            html_text = etree.HTML(res.text, etree.HTMLParser())
            result = html_text.xpath("//div[@id='all-list']//li[@class='video-item matrix']/a/@href")
            if len(result) == 0:
                break
            consumer1 = threading.Thread(target=thread_download_video,args=(result, dirpath))
            consumer2 = threading.Thread(target=thread_download_video, args=(result, dirpath))
            consumer3 = threading.Thread(target=thread_download_video, args=(result, dirpath))
            consumer1.start()
            consumer2.start()
            consumer3.start()
            consumer1.join()
            consumer2.join()
            consumer3.join()
    except Exception as e:
        print("download_video 出错，未下载成功：", e)
        time.sleep(8)

def main():
    try:
        keyWords = input(r"请输入你要下载的视频关键词: ")
        print("开始下载 ", keyWords, " 关键字视频！！！")
        print("=" * 50)
        dirpath = os.path.join(os.getcwd(), "bilibili_video_"+keyWords)
        makeDir(dirpath)
        urls = buildUrls(keyWords)
        download_video(urls, dirpath)
    except Exception as e:
        print("运行出错：", e)
        time.sleep(8)

if __name__ == '__main__':
    main()
