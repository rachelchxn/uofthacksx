import yt_dlp as youtube_dl
import os

class CoolClass:
    def __init__(self):
        self.options = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'keepvideo':False,
            'outtmpl': 'temp.mp3'
        }

    def download_file(self,url):
        try:
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = url,download=False
            )
            video_title = video_info['title']
            originalfilename = video_title + '.mp3'
            self.options['outtmpl'] = originalfilename
            with youtube_dl.YoutubeDL(self.options) as ydl:
                ydl.download([video_info['webpage_url']])
        except youtube_dl.utils.DownloadError: 
            print('invalid URL!')
        

a = CoolClass()

song = 'https://www.youtube.com/watch?v=vjplIOhE9So&ab_channel=ABOUTPOK%C3%A8MON'
a.download_file(song)