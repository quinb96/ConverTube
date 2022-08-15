from format_converter import *
from link_parser import *
from thumbnail_preview_window import *
from ConverTube import *
import os
import sys
import subprocess
from PySide2 import *

#Use the ffmpeg cli program for windows version.
#Must have ffmpeg.exe and its dependencies in the same folder as the main python script
#The ffmpeg-python lib only returns a TypeError stating that it can't find any
#file in the Windows filesystem
#Adding the ffmpeg\bin folder to the system-wide and user environment variables
#then running that does that same thing

class ResolutionDownloader(QRunnable):
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
            video_stream = video.streams.get_by_itag(17)
            file_name = os.path.abspath(video_stream.download())
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, file_name)
            self.fmt_cvrter_thread.start(format_converter)

        elif self.resolution_selector == "240p":
            print("240p has been selected!")
            if sys.platform == "linux" or sys.platform == "linux2":
                video_stream = video.streams.get_by_itag(133)
                video_name = os.path.abspath(video_stream.download())
                video_codec = ffmpeg.input(video_name)
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(audio_stream.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)

            elif sys.platform == "win32":
                video_stream = video.streams.get_by_itag(137)
                video_name = os.path.basename(video_stream.download())
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.basename(audio_stream.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-crf", "0", "-c:v", "copy",
                                 "-c:a", "copy", "-strict", "-2", video_name[:-4] + "(1).mp4"])
            media_container = os.path.abspath(video_name)
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)

        elif self.resolution_selector == "360p":
            video_stream = video.streams.get_by_itag(18)
            file_name = os.path.abspath(video_stream.download())
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, file_name)
            self.fmt_cvrter_thread.start(format_converter)

        elif self.resolution_selector == "480p":
            print("480p has been selected")
            if sys.platform == "linux" or sys.platform == "linux2":
                video_stream = video.streams.get_by_itag(135)
                video_name = os.path.abspath(video_stream.download())
                video_codec = ffmpeg.input(video_name)
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(audio_stream.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)

            elif sys.platform == "win32":
                video_stream = video.streams.get_by_itag(137)
                video_name = os.path.basename(video_stream.download())
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.basename(audio_stream.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-q:v", "0", "-map",
                                 "0:v", "-map", "1:a", video_name[:-4] + "(1).mp4"])
            media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)

        elif self.resolution_selector == "720p":
            if sys.platform == "linux" or sys.platform == "linux2":
                video_stream = video.streams.get_by_itag(22)
                file_name = os.path.abspath(video_stream.download())
                format_converter = FormatConverter(self.format_selector, file_name)
                self.fmt_cvrter_thread.start(format_converter)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000  # 5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            elif sys.platform == "win32":
                video_stream = video.streams.get_by_itag(22)
                file_name = os.path.abspath(video_stream.download())
                format_converter = FormatConverter(self.format_selector, file_name)
                self.fmt_cvrter_thread.start(format_converter)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000  # 5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)


        elif self.resolution_selector == "1080p":
            if sys.platform == "linux" or sys.platform == "linux2":
                video_stream = video.streams.get_by_itag(137)
                video_name = os.path.abspath(video_stream.download())
                video_codec = ffmpeg.input(video_name)
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(audio_stream.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)

            elif sys.platform == "win32":
                video_stream = video.streams.get_by_itag(137)
                video_name = os.path.basename(video_stream.download())
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.basename(audio_stream.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-q:v", "0", "-map",
                                 "0:v", "-map", "1:a", video_name[:-4] + "(1).mp4"])
            media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)

        elif self.resolution_selector == "1440p":
            if sys.platform == "linux" or sys.platform == "linux2":
                video_stream = video.streams.get_by_itag(400)
                video_name = os.path.abspath(video_stream.download())
                video_codec = ffmpeg.input(video_name)
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(audio_stream.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)
                os.remove(video_name)
                os.remove(audio_name)

            elif sys.platform == "win32":
                video_stream = video.streams.get_by_itag(400)
                video_name = os.path.basename(video_stream.download())
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.basename(audio_stream.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-q:v", "0", "-map",
                                 "0:v", "-map", "1:a", video_name[:-4] + "(1).mp4"])
            media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)

        elif self.resolution_selector == "2160p":
            if sys.platform == "linux" or sys.platform == "linux2":
                video_stream = video.streams.get_by_itag(401)
                video_name = os.path.abspath(video_stream.download())
                video_codec = ffmpeg.input(video_name)
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.abspath(audio_stream.download())
                audio_codec = ffmpeg.input(audio_name)
                ffmpeg_conversion = ffmpeg.concat(video_codec, audio_codec, v=1, a=1).output(video_name[:-4] + "(1).mp4")
                ffmpeg.run(ffmpeg_conversion)
                media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
                format_converter = FormatConverter(self.format_selector, media_container)
                self.fmt_cvrter_thread.start(format_converter)
                os.remove(video_name)
                os.remove(audio_name)

            elif sys.platform == "win32":
                video_stream = video.streams.get_by_itag(137)
                video_name = os.path.basename(video_stream.download())
                audio_stream = video.streams.get_by_itag(251)
                audio_name = os.path.basename(audio_stream.download())
                subprocess.call(["ffmpeg", "-i", video_name, "-i", audio_name, "-q:v", "0", "-map",
                                 "0:v", "-map", "1:a", video_name[:-4] + "(1).mp4"])
            media_container = os.path.abspath(video_name[:-4] + "(1).mp4")
            system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
            duration = 5000 #5 seconds
            tray = QSystemTrayIcon(system_tray_icon)
            tray.show()
            tray.showMessage("ConverTube", "Finished downloading " + video_stream.title, system_tray_icon, duration)
            format_converter = FormatConverter(self.format_selector, media_container)
            self.fmt_cvrter_thread.start(format_converter)
            os.remove(video_name)
            os.remove(audio_name)