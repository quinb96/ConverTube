from settings_window import *
from PySide2 import *
from configparser import ConfigParser
import configparser
import os

class SettingsWindowLoader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Settings_Window() #Initializes main window
        self.ui.setupUi(self)  #Loads widgets to main window
        self.clickPosition = QtCore.QPoint()
        #self.mouseMoveEvent = self.mouseMoveEvent  #e variable automatically gets passed when calling function in this way
        self.center_window()  #Calling user defined center function
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  #Removes toolbar from window
        self.app_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
        self.setWindowIcon(self.app_icon)
        self.setFixedSize(708, 455)

        #Initializes configuration writers
        self.videoconfigparser = ConfigParser()
        self.audioconfigparser = ConfigParser()

        #Reading config files to determine where to save vidoes and audio
        self.videoconfigparser.read("video_save_path_config.cfg")
        self.audioconfigparser.read("audio_save_path_config.cfg")

        #Applying text to video and audio save location fields
        self.ui.video_save_path.setText(self.videoconfigparser.get("video_path", "video_save_path"))
        self.ui.audio_save_path.setText(self.audioconfigparser.get("audio_path", "audio_save_path"))

        #Toolbar functions
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())

        #Button functions
        self.ui.vidlocbrowser_button.clicked.connect(lambda: self.init_videofilebrowser())
        self.ui.audlocbrowser_button.clicked.connect(lambda: self.init_audiofilebrowser())

    #Center the window on the screen
    def center_window(self):
        self.alignment_handler = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center() #Center declaration
        self.alignment_handler.moveCenter(self.cp) #Action of moving the window. Function is deprecated and no longer works on it's own. It needs the self.move() function in order to work now..
        self.move(self.alignment_handler.topLeft()) #Makes alignment_handler.moveCenter() work. This method is what actually centers the window

    #Move window on mouse drag event
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton: #If left button is held down.
            self.move(self.pos() + e.globalPos() - self.clickPosition) #Move window with mouse
            self.clickPosition = e.globalPos() #Assigning clickPosition the global window position value.
            e.accept() #Window sits where user releases the left clicker

    #Initialize video file browser
    def init_videofilebrowser(self):
        self.video_save_path_selector = VideoFileBrowser(self.ui.video_save_path, self.ui.video_save_button)
        self.video_save_path_selector.select_video_save_directory()

    #Initialize audio file browser
    def init_audiofilebrowser(self):
        self.audio_path_selector = AudioFileBrowser(self.ui.audio_save_path, self.ui.audio_save_button)
        self.audio_path_selector.select_audio_save_directory()

class VideoFileBrowser(QDialog):
    def __init__(self, video_save_path, video_save_button):
        super().__init__()
        self.video_save_path = video_save_path
        self.video_save_button = video_save_button

    def select_video_save_directory(self):
        self.video_directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.video_save_path.setText(self.video_directory)
        self.video_save_button.clicked.connect(lambda:self.write_to_video_config(self.video_directory))

    def write_to_video_config(self, video_save_path):
        self.config = ConfigParser()
        self.video_save_path = video_save_path
        self.config["video_path"] = {
            "video_save_path": self.video_save_path
        }
        #Write to config file
        with open("video_save_path_config.cfg", "w") as configfile:
            self.config.write(configfile)

class AudioFileBrowser(QDialog):
    def __init__(self, audio_save_path, audio_save_button):
        super().__init__()
        self.audio_save_path = audio_save_path
        self.audio_save_button = audio_save_button

    def select_audio_save_directory(self):
        self.audio_directory = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.audio_save_path.setText(self.audio_directory)
        self.audio_save_button.clicked.connect(lambda: self.write_to_audio_config(self.audio_directory))

    def write_to_audio_config(self, audio_save_path):
        self.config = ConfigParser()
        self.audio_save_path = audio_save_path
        self.config["audio_path"] = {

            "audio_save_path": self.audio_save_path
        }
        #Write to config file
        with open("audio_save_path_config.cfg", "w") as configfile:
            self.config.write(configfile)