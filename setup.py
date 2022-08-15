import sys
import os
import shutil
from setuptools import setup, find_packages

def success_msg():
    print("Installation successful!\nExiting setup script...")

def path_checker():
    print("Application is already installed.\nExiting setup script...")

def unpack_files():
    #Function will check if device is Windows.
    #If it is, copy app files to ~/Program_Files(x86)
    if sys.platform == "linux" or sys.platform == "linux2":
        try:
            shutil.copytree("../ConverTube", os.path.expanduser(os.environ["HOME"] + "/.local/ConverTube")) #Unpacking files
        except IOError:
            #If the folder already exists
            if os.path.exists(os.environ["HOME"] + "/.local/ConverTube"):
                path_checker()
                sys.exit(1) #Exit setup script
            else:
                pass #Otherwise, do nothing
    elif sys.platform == "win32":
        print("Windows OS detected from unpack_files()!")

def make_shortcut():
    if sys.platform == "linux" or sys.platform == "linux2":
        shortcutinfo = """[Desktop Entry]
Name=ConverTube
Version=1.0
Icon=/home/quin/.local/ConverTube/assets/CT_app_icon.ico
Exec=python3 /home/quin/.local/ConverTube/ConverTube.py
Terminal=False
Type=Application"""
        with open("/home/quin/Desktop/ConverTube.desktop", "w") as desktopshortcutwriter:
            desktopshortcutwriter.write(shortcutinfo)
        desktopshortcutwriter.close()
    elif sys.platform == "win32":
        #No process for Windows yet
        print("Windows OS detected from make_shortcut()!")
        #Make function that copies packages to ~/Program_Files(x86)

setup(
    name='ConverTube',
    version='1.0',
    packages=find_packages(),
    url='',
    author='Quin Brown',
    author_email='quinb96@protonmail.com',
    description='A multithreaded YouTube video downloader and converter',
    install_requires=["pyside2",
                      "pyqt5",
                      "pytube",
                      "ffmpeg-python",
                      "youtube_dl"
    ]
)

unpack_files()
#make_shortcut()
success_msg()
sys.exit(1)
