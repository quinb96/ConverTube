import urllib.request
import sys
import os
import zipfile
from acc_den_err_win_loader import *
from yt_qry_err_win_loader import *
from convertube_splash_screen import *
from configparser import ConfigParser
from thumbnail_preview_window_loader import *
from settings_window_loader import *
from link_parser import *
from main_window import *
from about_window_loader import *

progressBarValue = 0

class SplashLoader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash_Window()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centerWindow()
        self.app_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
        self.setWindowIcon(self.app_icon)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)
        self.timer.start(100) #Start progress bar
        self.show()

    #Checks the websites status code
    #Refactor function to display the error window
    def checkYTStatus(self):
        return urllib.request.urlopen("https://www.youtube.com/").getcode()

    def appProgress(self):
        # Access the global variable progressBarValue
        global progressBarValue

        # Apply progressBarValue to the progressBar
        self.ui.progressBar.setValue(progressBarValue)

        if progressBarValue > 100:
            QtCore.QTimer.singleShot(0, lambda: self.ui.status_text.setText("Done!"))
            self.timer.stop()
            self.close()
            self.mainwindow = MainWindowLoader()
            self.mainwindow.show()
            tray.showMessage("ConverTube", "ConverTube has started!", system_tray_icon, duration)


        #Lets update the loading status text as the progress changes
        elif progressBarValue < 20:
            self.ui.status_text.setText("Querying YouTube...")

            #If checkYTStatus returns code 200
            if self.checkYTStatus() == 200:
                #Update text
                QtCore.QTimer.singleShot(0, lambda: self.ui.status_text.setText("OK!"))
            else:
                self.timer.stop() #Stop progress bar
                self.yt_err_win = YTWryErrWinLoader() #Initialize window
                self.yt_err_win.show() #Display window
                self.close() #Close app


        elif progressBarValue < 55:
            QtCore.QTimer.singleShot(0, lambda: self.ui.status_text.setText("Configuring..."))

            #If config file doesn't exist
            if not os.path.exists("video_save_path_config.cfg"):
                #Initialize the config parser
                self.videoconfigparser = ConfigParser()
                self.video_save_path = os.path.join(os.path.expanduser("~"), "Videos")
                self.videoconfigparser["video_path"] = {
                    "video_save_path": self.video_save_path
                }
                #Error handling
                try:
                    #Write the config file
                    with open("video_save_path_config.cfg", "w") as configfile:
                        self.videoconfigparser.write(configfile)
                        configfile.close()
                #If program fails to write config file
                except PermissionError:
                    self.timer.stop() #Stop progress bar
                    self.access_denied_window = AccDenErrWinLoader() #Initialize error window
                    self.access_denied_window.show() #Display error window

            #If config file doesn't exist
            elif not os.path.exists("audio_save_path_config.cfg"):
                #Initialize the config parser
                self.audioconfigparser = ConfigParser()
                self.audio_save_path = os.path.join(os.path.expanduser("~"), "Music")
                self.audioconfigparser["audio_path"] = {
                    "audio_save_path": self.audio_save_path
                }
                try:
                    #Write the config file
                    with open("audio_save_path_config.cfg", "w") as configfile:
                        self.audioconfigparser.write(configfile)
                        configfile.close()
                except PermissionError:
                    self.timer.stop() #Stop progress bar
                    self.access_denied_window = AccDenErrWinLoader()  #Initialize error window
                    self.access_denied_window.show()  #Display error window
            else:
                #Do nothing
                pass

        elif progressBarValue < 70:
            if not os.path.exists("ffmpeg"):
                QtCore.QTimer.singleShot(0, lambda: self.ui.status_text.setText("Unpacking FFmpeg..."))
                ffmpeg_zipfile = zipfile.ZipFile("ffmpeg.zip")
                ffmpeg_zipfile.extractall("ffmpeg")
                ffmpeg_exe = "ffmpeg/ffmpeg-n5.0-latest-win64-lgpl-5.0/bin/ffmpeg.exe"
                ffplay_exe = "ffmpeg/ffmpeg-n5.0-latest-win64-lgpl-5.0/bin/ffplay.exe"
                ffprobe_exe = "ffmpeg/ffmpeg-n5.0-latest-win64-lgpl-5.0/bin/ffprobe.exe"
                shutil.copy(ffmpeg_exe, "../ConverTube/")
                shutil.copy(ffplay_exe, "../ConverTube")
                shutil.copy(ffprobe_exe, "../ConverTube")
            else:
                #Do nothing
                pass



        #assignedEnvVar = shutil.move(os.environ["USERPROFILE"] + "\Program Files\ffmpeg\bin")

        elif progressBarValue < 99:
            QtCore.QTimer.singleShot(0, lambda: self.ui.status_text.setText("Initializing window..."))
        progressBarValue += 1

    #Center the window on the screen
    def centerWindow(self):
        alignment_handler = self.frameGeometry()
        center_window = QDesktopWidget().availableGeometry().center() #Center declaration
        alignment_handler.moveCenter(center_window) #Action of moving the window. Function is deprecated and no longer works on it's own. It needs the self.move() function in order to work now
        self.move(alignment_handler.topLeft()) #Makes alignment_handler.moveCenter() work. This method is what actually centers the window

#Global window value
WINDOW_SIZE = 0
#This help the program determine if the window minimized or maximized

class MainWindowLoader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.linkparsethread = threading.Thread(target=self.call_youtube) #Initializes thread
        #self.linkparsethread.start() #Starts thread
        #self.linkparsethread.join() #Waits until thread is finished before moving further
        self.threadpool = QThreadPool()
        self.ui = Ui_MainWindow() #Initializes main window
        self.ui.setupUi(self) #Loads widgets to main window
        self.clickPosition = QtCore.QPoint()
        self.mouseMoveEvent = self.mouseMoveEvent #e variable automatically gets passed when function is called without parenthesis
        self.centerWindow() #Calling user defined center function
        self.show() #Displays main window and UI
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Removes toolbar from window
        self.setWindowIcon(QtGui.QIcon(app_icon)) #Displays icon in taskbar

        #Toolbar functions
        #self.ui.hamburger_button.clicked.connect(lambda: self.slideLeftMenu()) #Calls slideLeftMenu function
        self.ui.exit_button.clicked.connect(lambda: self.close()) #Exits app
        self.ui.maximize_button.clicked.connect(lambda: self.maximizeOrRestoreWindow()) #Calls max or restore window function
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized()) #Minimizes window
        self.ui.hamburger_button.clicked.connect(lambda: self.slideLeftMenu())

        #Button functions
        self.ui.start_button1.clicked.connect(lambda: self.parseLink(self.ui.url_textfield1.text()))
        self.ui.start_button2.clicked.connect(lambda: self.parseLink(self.ui.url_textfield2.text()))
        self.ui.start_button3.clicked.connect(lambda: self.parseLink(self.ui.url_textfield3.text()))
        self.ui.start_button4.clicked.connect(lambda: self.parseLink(self.ui.url_textfield4.text()))
        self.ui.start_button5.clicked.connect(lambda: self.parseLink(self.ui.url_textfield5.text()))
        self.ui.settings_button.clicked.connect(lambda: self.openSettingsWindow())
        self.ui.help_button.clicked.connect(lambda: self.openAboutWindow())

    def splashThread(self):
        self.splash_thread = SplashLoader()
        self.splash_thread.show()

    def openAboutWindow(self):
        self.aboutWindow = AboutWindowLoader()
        self.aboutWindow.show()

    #Example code
    #Need to turn this into code that will first query YouTube to check for it's status code
    #Then parse the link in the edit text box using regex
    def parseLink(self, link):
        self.link = link
        self.link_parser_thread = LinkParser(self.link)
        self.threadpool.start(self.link_parser_thread)
        self.openThumbnailPreviewWindow(self.link)

    def openThumbnailPreviewWindow(self, link):
        self.link = link
        self.thumbnail_preview = ThumbnailPreviewWindowLoader(self.link)
        self.thumbnail_preview.show()

    def openSettingsWindow(self):
        self.settings_window = SettingsWindowLoader()
        self.settings_window.show()


    #Move window on mouse drag event
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton: #If left button is held down.
            self.move(self.pos() + e.globalPos() - self.click_position) #Move window with mouse
            self.click_position = e.globalPos() #Assigning click_position the global window position value.
            e.accept() #Window sits where user releases the left clicker

    #Center the window on the screen
    def centerWindow(self):
        alignment_handler = self.frameGeometry()
        center_window = QDesktopWidget().availableGeometry().center() #Center declaration
        alignment_handler.moveCenter(center_window) #Action of moving the window. Function is deprecated and no longer works on it's own. It needs the self.move() function in order to work now..
        self.move(alignment_handler.topLeft()) #Makes alignment_handler.moveCenter() work. This method is what actually centers the window

    #Check the websites status code
    #Print function is a place holder. Need to eventually get rid of it and
    #Make the function end with a "return" statement
    def checkYTStatus(self):
        print(urllib.request.urlopen("https://www.youtube.com/").getcode())

    #Expanding left menu
    def slideLeftMenu(self):
        width = self.ui.left_menu.width()

        #If left menu is miminized
        if width == 0:
            newWidth = 41 #Expand menu
        #If left menu is maximized
        else:
            newWidth = 0 #Restore menu

        #Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    #Maximize or restore window size
    def maximizeOrRestoreWindow(self):
        #Global windows state
        global WINDOW_SIZE
        win_status = WINDOW_SIZE #Global value equals 0 as defined at the top of the script
        #left_menu_height = self.ui.left_menu.height() #Fetch left menus current height

        if win_status == 0:
            #If the window is not maximized
            WINDOW_SIZE = 1
            self.showMaximized() #Maximize window
        else:
            WINDOW_SIZE = 0
            self.showNormal() #Restore window to original size

        #if left_menu_height == 330:
         #   newHeight = 700
        #else:
            #newHeight = 330

        #self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumHeight")
        #self.animation.setDuration(250)
        #self.animation.setStartValue(left_menu_height)
        #self.animation.setEndValue(newHeight)
        #self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        #self.animation.start()

    def finishedDownloadingTrayMessage(self, tray_message):
        system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
        duration = 5000  #5 seconds
        tray = QSystemTrayIcon(system_tray_icon, app)
        tray.show()
        tray.showMessage("ConverTube", tray_message, system_tray_icon, duration)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    #Declaring icon that shows in the taskbar
    app_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
    #Icon that shows in the system tray.
    splashwindow = SplashLoader()
    splashwindow.show()
    window = MainWindowLoader()

    #System tray elements
    system_tray_icon = QIcon(u":/icons/assets/CT_app_icon.ico")
    menu = QMenu() #Tray menu
    duration = 3000  #3 seconds
    open_action = menu.addAction("Open")
    open_action.triggered.connect(lambda: window.showNormal())
    settings_action = menu.addAction("Settings")
    settings_action.triggered.connect(lambda: window.openSettingsWindow())
    exit_action = menu.addAction("Exit")
    exit_action.triggered.connect(app.quit) #Exits app
    tray = QSystemTrayIcon(system_tray_icon, app)
    tray.setToolTip("ConverTube")
    tray.setContextMenu(menu)
    tray.show() #Displays menu when right clicked

    if not QSystemTrayIcon.isSystemTrayAvailable():
        #If no system tray is found
        QMessageBox.critical(None, "ConverTube", "ConverTube didn't detect a system tray. Exiting app.") #Display critical message
        time.sleep(10) #Sleep for 10 secs
        sys.exit(1) #Exits app
    sys.exit(app.exec_()) #Exits app

