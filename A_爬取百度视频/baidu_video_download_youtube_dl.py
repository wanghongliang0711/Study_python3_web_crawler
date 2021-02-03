"""
@author: wanghongliang
@file: baidu_video_download.py
@time: 2021/1/28 10:40 
"""
import requests, os, itertools
import urllib.parse
from lxml import html
import threading
# from you_get import common
# import sys

glock = threading.Lock()
etree = html.etree
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              "Host":"v.baidu.com"}

videoUrls = []
dirpath = ""


# 创建文件夹
def makeDir(dirpath):
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)


# 生成网址列表
def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://v.baidu.com/v?word={word}&ct=301989888&rn=67&pn={pn}&db=0&s=0&fbl=800&ie=utf-8"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=20))
    return urls


#生产者：源源不断产生图片网址并存入列表
def get_video_url(urls):
    try:
        global videoUrls
        for url in urls:
            print(url)
            res = requests.get(url, timeout=10, headers=header, allow_redirects=False)
            # print(res.text)
            html_text = etree.HTML(res.text, etree.HTMLParser())
            result = html_text.xpath("//div[@id='widget_normalresult']//li[@class='result']/a/@href")
            if len(result) == 0:
                break
            videoUrls = videoUrls + result
    except Exception as e:
        print("get_video_url 出错，未下载成功：", e)


""" 
https://github.com/ytdl-org/youtube-dl
youtube-dl




"""
def download_one_video(url, dirpath):
    try:
        url = "http://v.baidu.com" + url
        # print("开始下载： ", url)
        res = requests.get(url, timeout=10, headers=header, allow_redirects=False)
        html_text = etree.HTML(res.text, etree.HTMLParser())
        result = html_text.xpath("//a[@id='link']/@href")
        # print(result)
        if len(result) == 1:
            print("开始下载： ", result[0])
            # 下载 系列 视频     debug模式   不合并视频     不下载弹幕、字幕等
            # sys.argv = ['you-get', '-o', dirpath, '-l', '--debug', '--no-caption', '--no-merge', '-a', result[0]]
            # common.main()
            # plug_path = os.path.join(os.getcwd(), "plug_in", "you-get.exe")
            # zhiling = ('"{plug_path}" -o "{path}" -l --no-caption --no-merge -a {url}'.format(plug_path=plug_path, path=dirpath, url=result[0]))
            zhiling = ('plug_in\you-get.exe -o "{path}" -l --no-caption --no-merge -a {url}'.format(path=dirpath, url=result[0]))
            print(zhiling)
            success_result = os.system(zhiling)
            if success_result == 0:
                print(result[0], "下载成功。")
            else:
                print(result[0], "下载失败！！！")
    except Exception as e:
        print(url, "下载出错，未下载成功：", e)


def download_video():
    try:
        while True:
            global glock
            glock.acquire()
            global videoUrls
            global dirpath
            if len(videoUrls) == 0:
                glock.release()
                break
            else:
                url = videoUrls.pop()
                glock.release()
                download_one_video(url, dirpath)
    except Exception as e:
        print("download_video 出错，未下载成功：", e)


def main():
    try:
        keyWords = "car"

        plug_path = os.path.join(os.getcwd(), "plug_in", "you-get.exe")
        if os.path.exists(plug_path):
            print(f"开始下载 {keyWords} 关键字视频！！！")
            print("=" * 50)

            # 创建文件夹
            global dirpath
            dirpath = os.path.join(os.getcwd(), "video_"+keyWords)
            makeDir(dirpath)

            # 生成 url
            urls = buildUrls(keyWords)

            get_video_url(urls)
            global videoUrls
            videoUrls = list(set(videoUrls))
            print("一共有 %s 个video 会被下载" % (len(videoUrls)))
            # download_video()
            for x in range(3):
                consumer = threading.Thread(target=download_video)
                consumer.start()
        else:
            print("缺少 %s"%(plug_path))
    except Exception as e:
        print("运行出错：", e)

if __name__ == '__main__':
    main()





