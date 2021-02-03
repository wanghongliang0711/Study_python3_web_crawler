"""
@author: wanghongliang
@file: baidu_tupian_download_car_threading.py
@time: 2021/1/27 13:21 
"""
import requests, re, os, itertools, threading
import urllib.parse

str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36; charset=UTF-8",
              "Host":"tupian.baidu.com","Referer":"http://tupian.baidu.com/"}

char_table = {ord(key): ord(value) for key, value in char_table.items()}

really_imageUrls = []
glock = threading.Lock()
index = 0
dirpath = ""


def decodeUrl(url):
    # 先替换字符串
    for key, value in str_table.items():
        url = url.replace(key, value)
    # 再替换剩下的字符
    return url.translate(char_table)



# 创建文件夹
def makeDir(dirpath):
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)


# 生成网址列表
def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://tupian.baidu.com/search/acjson?" \
          r"tn=resultjson_com&logid=10490380256679113949&ipn=rj&" \
          r"ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&ic=0&" \
          r"word={word}&face=0&istype=2&nc=1&force=&pn={pn}&rn=30"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=30))
    return urls


def resolveImgUrl(html):
    result = re.findall(r'"objURL":"(.*?)"', html)
    return [decodeUrl(x) for x in result]


def downImg(imgUrl, dirpath, imgName):
    filename = os.path.join(dirpath, imgName)
    try:
        print("开始下载： ", imgName)
        headers = { 'Connection': 'close', }
        res = requests.get(imgUrl, timeout=10, headers=headers)
        if str(res.status_code)[0] == "4":
            print(imgName, str(res.status_code), ":" , imgUrl)
            return
        with open(filename, "wb") as f:
            f.write(res.content)
    except Exception as e:
        print(imgName, "下载出错，未下载成功：", imgUrl)
        print(e)


def reallyImageUrls(urls):
    result = []
    for url in urls:
        html = requests.get(url, timeout=10, headers=header, allow_redirects=False).content.decode('utf-8')
        print(url)
        imgUrls = resolveImgUrl(html)
        result = result + imgUrls
        if len(imgUrls) == 0:
            break
    print("一共 ", len(result), " 张图片将会被下载！")
    return result


def download_picture():
    while True:
        global glock
        glock.acquire()
        global really_imageUrls
        global index
        global dirpath
        index += 1
        if len(really_imageUrls) == 0:
            glock.release()
            break
        else:
            url = really_imageUrls.pop()
            glock.release()
            downImg(url, dirpath, str(index) + ".jpg")


def main():
    try:
        keyWords = input(r"请输入你要下载的图片关键词: ")

        print("开始下载 ",keyWords, " 关键字图片！！！")
        print("=" * 50)

        # 创建文件夹
        global dirpath
        dirpath = os.path.join(os.getcwd(), keyWords)
        makeDir(dirpath)

        global really_imageUrls
        really_imageUrls = []
        # 生成 url
        # urls = buildUrls(keyWords)
        # urls 真实数量
        really_imageUrls = reallyImageUrls(buildUrls(keyWords))
        really_imageUrls.reverse()
        # 创建三个线程 下载
        for x in range(30):
            consumer = threading.Thread(target=download_picture)
            consumer.start()
    except Exception as e:
        print("运行出错：", e)


if __name__ == '__main__':
    main()
