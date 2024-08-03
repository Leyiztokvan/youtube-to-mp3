import yt_dlp
from pydub import AudioSegment
import os

def download_video_as_mp3(url, output_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_urls = [
    #"https://www.youtube.com/watch?v=example1",
    #"https://www.youtube.com/watch?v=example2",
    # Add more URLs as needed
    #
]

output_folder = 'mp3_files'
os.makedirs(output_folder, exist_ok=True)

for url in video_urls:
    download_video_as_mp3(url, output_folder)
    print(f'Downloaded and converted to MP3: {url}')
