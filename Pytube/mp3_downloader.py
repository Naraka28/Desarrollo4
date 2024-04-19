"""
Playlist downloader
"""

from pytube import Playlist, YouTube
p = Playlist("https://www.youtube.com/playlist?list=PLXboAJo1ui6EhhF6C0_nYsrY8Am8pO2QK")

print(f"Number of videos: {p.length}")
for i,video in enumerate(p.videos, start=1):
    yt=YouTube(video.watch_url)
    print(f"{i}. Author: {yt.author} Title: {yt.title} Length: {yt.length} Views: {yt.views}")
