import urllib.request
from resolution_downloader import *
from link_parser import *
from thumbnail_preview_window import *
from invalid_link_win_loader import *
from age_restr_win_loader import *
import sys


class ThumbnailPreviewWindowLoader(QMainWindow):
    def __init__(self, video_url):
        QMainWindow.__init__(self)
        self.ui = Ui_Thumbnail_Preview_Window()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Removes toolbar from window
        self.centerWindow()
        self.click_position = QtCore.QPoint()
        self.video_url = video_url
        self.fetch_thumbnail() #Fetching thumbnail url
        self.display_thumbnail()
        self.loadStreamsToComboboxes(self.video_url)
        self.resolution_downloader_thread = QThreadPool()
        self.app_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
        self.setWindowIcon(self.app_icon)

        #Toolbar functions
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.download_button.clicked.connect(lambda: self.startResolutionDownloaderThread(self.video_url))

    #Display thumbnail
    def display_thumbnail(self):
        if sys.platform == "win32":
            self.ui.thumbnail_preview.setPixmap(QPixmap(os.path.expanduser("~") + u"\\appdata\\Local\\Temp\\thumbnail.png"))
        elif sys.platform == "linux" or sys.platform == "linux2":
            self.ui.thumbnail_preview.setPixmap(QPixmap(os.path.expanduser("/tmp/thumbnail.png")))

    #Fetching thumbnail
    def fetch_thumbnail(self):
        try:
            self.video_thumbnail = pytube.YouTube(self.video_url).thumbnail_url  #Querying thumbnail url
            # If program fails to query thumbnail url
        except pytube.exceptions.RegexMatchError:
            self.invalid_link_window = InvalidLinkWinLoader() #Invalid Link Erorr Window
            self.invalid_link_window.show()
        if sys.platform == "win32":
            self.thumbnail_image = urllib.request.urlretrieve(self.video_thumbnail, os.path.expanduser("~\\appdata\\Local\\Temp\\thumbnail.png"))
        elif sys.platform == "linux" or sys.platform == "linux2":
            self.thumbnail_image = urllib.request.urlretrieve(self.video_thumbnail, os.path.expanduser("/tmp/thumbnail.png"))

    #Center the window on the screen
    def centerWindow(self):
        self.alignment_handler = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center() #Center declaration
        self.alignment_handler.moveCenter(self.cp) #Action of moving the window. Function is deprecated and no longer works on it's own. It needs the self.move() function in order to work now..
        self.move(self.alignment_handler.topLeft()) #Makes alignment_handler.moveCenter() work. This method is what actually centers the window

    #Load available resolutions to the resolution_selector(right) combobox
    def loadStreamsToComboboxes(self, video_url):
        self.video_url = video_url
        self.entered_link = [self.video_url]
        self.video = YouTube(str(self.entered_link))
        self.video_resolutions = [] #List of available resolutions

        try:
            #Loop through all of the available reoslutions and codecs
            for res in self.video.streams.filter(progressive=True).all():
                self.video_resolutions.append(res.resolution)
                print(self.video_resolutions)
            self.ui.resolution_selector.addItems(self.video_resolutions)
        except KeyError:
            self.agerestrwin = AgeRestrWinLoader() #Age Restricted Window
            self.agerestrwin.show()

        if self.video.streams.get_by_itag(133):
            self.ui.resolution_selector.addItem("240p") #Remove this
        else:
            pass

        if self.video.streams.get_by_itag(137):
            self.ui.resolution_selector.addItem("1080p")
        else:
            pass

        if self.video.streams.get_by_itag(400):
            self.ui.resolution_selector.addItem("1440p")
        else:
            pass

        if self.video.streams.get_by_itag(401):
            self.ui.resolution_selector.addItem("2160p")
        else:
            pass

    #Starts video downloading thread
    def startResolutionDownloaderThread(self, video_url):
        self.close()
        self.resolution_downloader = ResolutionDownloader(video_url, self.ui.resolution_selector.currentText(), self.ui.format_selector.currentText())
        self.resolution_downloader_thread.start(self.resolution_downloader)