"""
@author: wanghongliang
@file: study_02-asyncio.py
@time: 2020/6/30 19:48 
"""
import asyncio

"""
asyncio.gather   asyncio.wait
asyncio.set_event_loop


sem = asyncio.Semaphore(100)  # 维持100个信号量
tasks = [asyncio.ensure_future(fn(i, sem)) for i in range(1, 143)]

"""


"""
同步代码
"""
import time

# def hello():
#     time.sleep(1)
# def run():
#     for i in range(5):
#         hello()
#         print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！
# run()
"""
Hello World:1593601235.360317
Hello World:1593601236.3753593
Hello World:1593601237.3760712
Hello World:1593601238.390626
Hello World:1593601239.4051228
"""


"""
异步代码
这个还是和同步代码效果一样
"""

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(3, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())  python3.7

loop = asyncio.get_event_loop()
task1 = loop.create_task(say_after(3, "wang"))
task2 = loop.create_task(say_after(1, "liang"))
async def main1():
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")



loop.run_until_complete(main1())


# https://www.cnblogs.com/yy-cola/p/9532007.html
# python asyncio  aiohttp

# https://www.jianshu.com/p/5f41d9fb6b12


import asyncio
import time
start = time.time()
#定义第1个协程，协程就是将要具体完成的任务，该任务耗时3秒，完成后显示任务完成
async def to_do_something(i):
    print('第{}个任务：任务启动...'.format(i))
    #遇到耗时的操作，await就会使任务挂起，继续去完成下一个任务
    await asyncio.sleep(i)
    print('第{}个任务：任务完成！'.format(i))
    return f"{i}"
#定义第2个协程，用于通知任务进行状态
async def mission_running():
    print('任务正在执行...')
    return "***"


#创建一个循环
loop = asyncio.get_event_loop()
#创建一个任务盒子tasks，包含了3个需要完成的任务
tasks = [asyncio.ensure_future(to_do_something(3)),
         asyncio.ensure_future(to_do_something(2)),
         asyncio.ensure_future(mission_running()),
         asyncio.ensure_future(to_do_something(1))]
#tasks接入loop中开始运行
result = loop.run_until_complete(asyncio.wait(tasks))
# movies = loop.run_until_complete(asyncio.gather(*tasks))  # ['3', '2', '***', '1']

end = time.time()
print(result)
# print(movies)
print(end-start)