"""
@author: wanghongliang
@file: login.py
@time: 2020/7/5 16:18 
"""
import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'
        ## 维持会话，自动处理cookies
        self.session = requests.Session()

    ## 解析出登录所需要的
    def token(self):
        token = None
        response = self.session.get(self.login_url, headers=self.headers)
        html = response.text
        if html:
            htmlEle = etree.HTML(html, etree.HTMLParser())
            token = htmlEle.xpath("//div[@id='login']//input[@name='authenticity_token']/@value")
        return token

    def login(self, email, password):
        # print(self.token())
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print(response.text)

            # self.dynamics(response.text)

    ## 关注人的动态信息


    ## 详情页面




if __name__ == "__main__":
    login = Login()
    login.login(email='wanghongliang0711', password='wang527486')
