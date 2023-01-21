import yt_dlp as youtube_dl
import os
import uuid

class CoolClass:
    def __init__(self):
        self.options = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'keepvideo':False,
            'outtmpl': 'temp.mp3'
        }

    def download_file(self,url):
        try:
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = url, download=False
            )
            originalfilename = str(uuid.uuid4())+'.mp3'
            self.options['outtmpl'] = originalfilename
            with youtube_dl.YoutubeDL(self.options) as ydl:
                ydl.download([video_info['webpage_url']])
        except youtube_dl.utils.DownloadError: 
            print('invalid URL!')  
    def download_yt(self):
        song = input('Youtube link: ')
        self.download_file(song)
        file = self.options['outtmpl']['default']
        return file
    # https://www.youtube.com/watch?v=1a8pI65emDE
    def test(self):
        print('testing')