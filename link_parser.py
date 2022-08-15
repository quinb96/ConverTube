import pytube
from PySide2 import *
import threading
import urllib.request
import time
from main_window import *
from pytube import *

class LinkParser(QRunnable):

    def __init__(self, yt_link):
        super().__init__()
        self.yt_link = yt_link

    def run(self):
        entered_link = [self.yt_link]
        video = YouTube(str(entered_link))