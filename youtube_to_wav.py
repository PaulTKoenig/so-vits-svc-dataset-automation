from __future__ import unicode_literals
import yt_dlp
import ffmpeg
import sys
import os

def youtube_to_wav():

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        # Read urls from text file urls.txt
        urls = []
        with open('urls.txt') as f:

            lines = f.readlines()
            for line in lines:
                line = line.replace("\n","")
                urls.append(line)

        # Download from url
        for url in urls:
            ydl.download([url])
            stream = ffmpeg.input('output.m4a')
            stream = ffmpeg.output(stream, 'output.wav')