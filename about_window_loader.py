from PySide2 import QtCore
from about_window import *

class AboutWindowLoader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_About_Window()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.OK_button.clicked.connect(lambda: self.close())


    def centerWindow(self):
        alignment_handler = self.frameGeometry()
        center_window = QDesktopWidget().availableGeometry().center() #Center declaration
        alignment_handler.moveCenter(center_window) #Action of moving the window. Function is deprecated and no longer works on it's own. It needs the self.move() function in order to work now..
        self.move(alignment_handler.topLeft()) #Makes alignment_handler.moveCenter() work. This method is what actually centers the window