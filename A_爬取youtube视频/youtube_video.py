"""
@author: wanghongliang
@file: youtube_video.py
@time: 2021/2/25 16:46 
"""
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

print(videosSearch.result())

# 因为被墙，所以。。。
