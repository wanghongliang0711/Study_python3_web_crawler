"""
@author: wanghongliang
@file: Tester.py
@time: 2020/7/5 14:01 
"""
from 第9章_代理的使用.第9_2代理池的维护.RedisClient import RedisClient
import asyncio
import aiohttp, time


BATCH_TEST_SIZE=100
VALID_STATUS_CODES=[200]
TEST_URL='http://www.baidu.com'
class Proxy_Tester(object):
    def __init__(self):
        self.redis = RedisClient()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.121 Safari/537.36"}

    async def test_single_proxy(self, proxy):
        """
        测试单个代理
        :param proxy: 单个代理
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(headers=self.headers, connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print("正在测试", proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print("代理可用", proxy)
                    else:
                        self.redis.decrease(proxy)
                        print("请求响应码不合法", proxy)
            except Exception as e:
                self.redis.decrease(proxy)
                print("代理请求失败 ", e)



    def run(self):
        """
        测试主函数
        :return:
        """
        print("----测试器运行-----")
        try:
            proxies = self.redis.all()
            loop = asyncio.get_event_loop()
            # 批量测试
            for i in range(0, len(proxies), BATCH_TEST_SIZE):  # 间隔BATCH_TEST_SIZE，相当于一次检测 BATCH_TEST_SIZE 个
                test_proxies = proxies[i:i+BATCH_TEST_SIZE]
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)

        except Exception as e:
            print("测试发生错误", e)

while True:
    d = Proxy_Tester()
    d.run()
    time.sleep(60)
