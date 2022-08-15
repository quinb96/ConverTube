from format_converter import *
from link_parser import *
from thumbnail_preview_window import *
import os
import sys
import subprocess
from PySide2 import *

class DownloadRes(QRunnable):
    def __init__(self, yt_link, resolution_selector, format_selector):
        super().__init__()
        self.yt_link = yt_link
        self.resolution_selector = resolution_selector
        self.format_selector = format_selector
        self.fmt_cvrter_thread = QThreadPool()

    def run(self):
        entered_link = [self.yt_link]
        video = YouTube(str(entered_link))

        if self.resolution_selector == "144p":
            res = video.streams.get_by_itag(17)
            res.download()

        elif self.resolution_selector == "240p":
            print("240p has been selected!")

        elif self.resolution_selector == "360p":
            res = video.streams.get_by_itag(18)
            res.download()

        elif self.resolution_selector == "480p":
            print("480p has been selected")

        elif self.resolution_selector == "720p":
            res = video.streams.get_by_itag(22)
            file_name = os.path.abspath(res.download())
            format_converter = FormatConverter(self.format_selector, file_name)
            self.fmt_cvrter_thread.start(format_converter)

        elif self.resolution_selector == "1080p":
            if sys.platform == "linux" or sys.platform == "linux2":
                res = video.streams.get_by_itag(137)
                video_name = os.path.abspath(res.download())
                video_codec = ffmpeg.input(video_name)
                aud = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(aud.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)
            #Use the ffmpeg cli program for windows version.
            #Must have ffmpeg.exe and its dependencies in the same folder as the main python script
            #The ffmpeg-python lib only returns a TypeError stating that it can't find any
            #file in the Windows filesystem
            #Adding the ffmpeg\bin folder to the system-wide and user environment variables
            #then running that does that same thing
            elif sys.platform == "win32":
                res = video.streams.get_by_itag(137)
                video_name = os.path.basename(res.download())
                aud = video.streams.get_by_itag(251)
                audio_name = os.path.basename(aud.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-crf", "0", "-c:v", "copy",
                                 "-c:a", "copy", "-strict", "-2", video_name)
                #Need to figure out how to convert videos without losing quality
                #Was keeping the quality on linux before but now it's reducing the quality on linux and Windows
                #after working on Windows specific code
            media_container = os.path.abspath(video_name) #Replace with video_name variable
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)

        elif self.resolution_selector == "1440p":
            if sys.platform == "linux" or sys.platform == "linux2":
                res = video.streams.get_by_itag(400)
                video_name = os.path.abspath(res.download())
                video_codec = ffmpeg.input(video_name)
                aud = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(aud.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)
                os.remove(video_name)
                os.remove(audio_name)

            elif sys.platform == "win32":
                res = video.streams.get_by_itag(400)
                video_name = os.path.basename(res.download())
                aud = video.streams.get_by_itag(251)
                audio_name = os.path.basename(aud.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-crf", "0", "-c:v", "copy",
                                 "-c:a", "copy", "-strict", "-2", "testout.mp4"])
            media_container = os.path.abspath("testout.mp4")
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)

        elif self.resolution_selector == "2160p":
            if sys.platform == "linux" or sys.platform == "linux2":
                res = video.streams.get_by_itag(401)
                video_name = os.path.abspath(res.download())
                video_codec = ffmpeg.input(video_name)
                aud = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(aud.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)
                os.remove(video_name)
                os.remove(audio_name)

            elif sys.platform == "win32":
                res = video.streams.get_by_itag(137)
                video_name = os.path.basename(res.download())
                aud = video.streams.get_by_itag(251)
                audio_name = os.path.basename(aud.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-crf", "0", "-c:v", "copy",
                                 "-c:a", "copy", "-strict", "-2", "testout.mp4"])
            media_container = os.path.abspath("testout.mp4")
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)