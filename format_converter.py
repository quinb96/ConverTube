import ffmpeg
import os
from resolution_downloader import *
from thumbnail_preview_window_loader import *
from ConverTube import *
from configparser import ConfigParser
import shutil
import sys
import subprocess
from PySide2 import *

class FormatConverter(QtCore.QRunnable):
    def __init__(self, format_selector, file_name):
        super().__init__()
        self.format_selector = format_selector
        self.file_name = file_name

    def run(self):
        if self.format_selector == "mp4":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-7] + "(2).mp4"])
                os.remove(self.file_name[:-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(2).mp4", config.get("video_path", "video_save_path"))
                except FileNotFoundError as SE: #If file already exists, have a dialog box pop up asking if they'd like to overwrite it
                    pass
                except PermissionError as PE: #If permission is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mp4",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".mkv"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).mkv", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mkv",
                                 system_tray_icon, duration)

        elif self.format_selector == "mkv":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".mkv"])
                #video_codec = ffmpeg.input(self.file_name)
                #stream = ffmpeg.output(video_codec, self.file_name[:-4] + ".mkv").run()
                os.remove(self.file_name[:-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".mkv", config.get("video_path", "video_save_path"))
                except FileNotFoundError as SE: #If file already exists, have a dialog box pop up asking if they'd like to overwrite it
                    pass
                except PermissionError as PE: #If permission is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mkv",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".mkv"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).mkv", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mkv",
                                 system_tray_icon, duration)

        elif self.format_selector == "avi":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".avi"])
                #video_codec = ffmpeg.input(self.file_name)
                #stream = ffmpeg.output(video_codec, self.file_name[:-4] + ".avi")
                #ffmpeg.run(stream)
                os.remove(self.file_name[:-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".avi", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to avi",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".avi"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).avi", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to avi",
                                 system_tray_icon, duration)

        elif self.format_selector == "mp3":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                video_codec = ffmpeg.input(self.file_name)
                audio_codec = video_codec.audio
                stream = ffmpeg.output(audio_codec, self.file_name[:-4] + ".mp3")
                ffmpeg.run(stream)
                os.remove(self.file_name)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".mp3", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    os.remove(self.file_name[:-4] + ".mp3")
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mp3",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".mp3"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).mp3", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mp3",
                                 system_tray_icon, duration)


        elif self.format_selector == "wav":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                video_codec = ffmpeg.input(self.file_name)
                audio_codec = video_codec.audio
                stream = ffmpeg.output(audio_codec, self.file_name[:-4] + ".wav")
                ffmpeg.run(stream)
                os.remove(self.file_name)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".wav", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    os.remove(self.file_name[:-4] + ".wav")
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to wav",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".wav"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).wav", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to wav",
                                 system_tray_icon, duration)

        elif self.format_selector == "wma":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".wma"])
                #video_codec = ffmpeg.input(self.file_name)
                #stream = ffmpeg.output(video_codec, self.file_name[:-4] + ".wma")
                #ffmpeg.run(stream)
                os.remove(self.file_name[:-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".wma", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to wma",
                                 system_tray_icon, duration)

            if sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".wma"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).wma", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to wma",
                                 system_tray_icon, duration)


        elif self.format_selector == "wmv":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".wmv"])
                #video_codec = ffmpeg.input(self.file_name)
                #stream = ffmpeg.output(video_codec, self.file_name[:-4] + ".wmv")
                #ffmpeg.run(stream)
                os.remove(self.file_name[-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".wmv", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to wmv",
                                 system_tray_icon, duration)

            if sys.platform == "win32":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".wmv"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).wmv", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to wmv",
                                 system_tray_icon, duration)

        elif self.format_selector == "flv": #Windows Media Player can't play flv. Check if any other multimedia program can play it
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".flv"])
                #video_codec = ffmpeg.input(self.file_name)
                #stream = ffmpeg.output(video_codec, self.file_name[:-4] + ".flv")
                #ffmpeg.run(stream)
                os.remove(self.file_name[:-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".flv", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to flv",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".flv"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).flv", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to flv",
                                 system_tray_icon, duration)

        elif self.format_selector == "flac":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                video_codec = ffmpeg.input(self.file_name)
                audio_codec = video_codec.audio
                stream = ffmpeg.output(audio_codec, self.file_name[:-4] + ".flac")
                ffmpeg.run(stream)
                os.remove(self.file_name)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".flac", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    os.remove(self.file_name[:-4] + ".flac")
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to flac",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".flac"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).flac", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to flac",
                                 system_tray_icon, duration)

        elif self.format_selector == "mov":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".avi"])
                #video_codec = ffmpeg.input(self.file_name)
                #stream = ffmpeg.output(video_codec, self.file_name[:-4] + ".mov")
                #ffmpeg.run(stream)
                os.remove(self.file_name[:-7] + "(1).mp4")
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".mov", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE: #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show() #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mov",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("video_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".mov"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).mov", config.get("video_path", "video_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to mov",
                                 system_tray_icon, duration)

        elif self.format_selector == "m4a":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                video_codec = ffmpeg.input(self.file_name)
                audio_codec = video_codec.audio
                stream = ffmpeg.output(audio_codec, self.file_name[:-4] + ".m4a")
                ffmpeg.run(stream)
                os.remove(self.file_name)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".m4a", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    os.remove(self.file_name[:-4] + ".m4a")
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to m4a",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".m4a"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).m4a", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to m4a",
                                 system_tray_icon, duration)

        elif self.format_selector == "aac":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                video_codec = ffmpeg.input(self.file_name)
                audio_codec = video_codec.audio
                stream = ffmpeg.output(audio_codec, self.file_name[:-4] + ".aac")
                ffmpeg.run(stream)
                os.remove(self.file_name)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".aac", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    os.remove(self.file_name[:-4] + ".aac")
                except PermissionError as PE:  #If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to aac",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".aac"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).aac", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to aac",
                                 system_tray_icon, duration)

        elif self.format_selector == "aiff":
            if sys.platform == "linux" or sys.platform == "linux2":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                video_codec = ffmpeg.input(self.file_name)
                audio_codec = video_codec.audio
                stream = ffmpeg.output(audio_codec, self.file_name[:-4] + ".aiff")
                ffmpeg.run(stream)
                os.remove(self.file_name)
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray = QSystemTrayIcon(system_tray_icon)
                tray.show()
                try:
                    shutil.move(self.file_name[:-4] + ".aiff", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    os.remove(self.file_name[:-4] + ".aiff")
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  # Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to aiff",
                                 system_tray_icon, duration)

            elif sys.platform == "win32":
                config = ConfigParser()
                config.read("audio_save_path_config.cfg")
                self.file_name = self.file_name
                subprocess.call(["ffmpeg", "-i", self.file_name, "-q:v", "0", self.file_name[:-4] + ".aiff"])
                try:
                    os.remove(self.file_name[:-7] + "(1).mp4")
                except:
                    pass
                system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
                duration = 5000 #5 seconds
                tray.show()
                try:
                    shutil.move(self.file_name[:-7] + "(1).aiff", config.get("audio_path", "audio_save_path"))
                except FileNotFoundError:
                    pass
                except PermissionError as PE:  # If access is denied at path
                    access_denied_window = acc_den_err_win_loader()
                    access_denied_window.show()  #Display error window
                tray.showMessage("ConverTube", os.path.basename(self.file_name[:-4]) + " has been converted to aiff",
                                 system_tray_icon, duration)
