import sys
import os
import shutil
import winshell
from win32com.client import Dispatch
from setuptools import setup, find_packages

def success_msg():
    print("Installation successful!\nExiting setup script...")

def path_checker():
    print("Application is already installed.\nExiting setup script...")

def unpack_files():
    #Function will check if device is Windows.
    #If it is, copy app files to ~/Program_Files(x86)
    #Run this script in cmd as admin so that the script has access admin privileges access to the Programs Files (x86) folder
    if sys.platform == "linux" or sys.platform == "linux2":
        try:
            shutil.copytree("../ConverTube", os.path.expanduser("/home/" + os.environ["SUDO_USER"] + "/.local/ConverTube")) #Unpacking files
        except IOError:
            #If the folder already exists
            if os.path.exists("/home/" + os.environ["SUDO_USER"] + "/.local/ConverTube"):
                path_checker()
                sys.exit(1) #Exit setup script
    elif sys.platform == "win32":
        try:
            shutil.copytree("../ConverTube", os.path.expanduser(os.environ["SYSTEMDRIVE"] + "/ConverTube")) #Unpacking files
        except IOError:
            if os.path.exists(os.environ["SYSTEMDRIVE"] + "/ConverTube"):
                path_checker()
                sys.exit(1)

def make_shortcut():
    if sys.platform == "linux" or sys.platform == "linux2":
        icon_path = os.path.expanduser("/home/" + os.environ["SUDO_USER"] + "/.local/share/applications/ConverTube.desktop")
        desktop_entry_header = "[Desktop Entry]"
        desktop_version = "Version=1.0"
        desktop_name = "Name=ConverTube"
        desktop_generic_name = "GenericName[en-US]=Video converter"
        desktop_comment = "Comment=Multimedia Downloader & Converter"
        desktop_exec = "Exec=sudo python3 " + os.path.expanduser("/home/" + os.environ["SUDO_USER"] + "/.local/ConverTube/ConverTube.py")
        desktop_path = "Path=" + os.path.expanduser("/home/" + os.environ["SUDO_USER"] + "/.local/ConverTube")
        desktop_icon = "Icon=" + os.path.expanduser("/home/" + os.environ["SUDO_USER"] + "/.local/ConverTube/assets/CT_app_icon.ico")
        desktop_terminal_boolean = "Terminal=true"
        desktop_type = "Type=Application"
        desktop_category = "Categories=Application"

        with open(icon_path, "w") as desktop_file:
            desktop_file.write(desktop_entry_header + "\n" + desktop_version + "\n" + desktop_name
                               + "\n" + desktop_generic_name + "\n" + desktop_comment + "\n" + desktop_exec
                               + "\n" + desktop_path + "\n" + desktop_icon + "\n" + desktop_terminal_boolean
                               + "\n" + desktop_type + "\n" + desktop_category)
            desktop_file.close()
    elif sys.platform == "win32":
        desktop = winshell.desktop()
        path = os.path.join(desktop, "ConverTube.lnk")
        target_path = os.path.expanduser(os.environ["SYSTEMDRIVE"] + "/ConverTube/ConverTube.py")
        working_directory = os.path.expanduser(os.environ["SYSTEMDRIVE"] + "\\ConverTube")
        desktop_icon = os.path.expanduser(os.environ["SYSTEMDRIVE"] + "/ConverTube/assets/CT_app_icon.ico")

        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.TargetPath = target_path
        shortcut.WorkingDirectory = working_directory
        shortcut.IconLocation = desktop_icon
        shortcut.save()

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
                      "youtube_dl"],
    classfiers=["Development Status :: 1 - Planning",
                "Intended Audience :: Average users",
                "Programming Language :: Python :: 3",
                "Operating System :: Unix",
                "Operating System :: Microsoft :: Windows"]
)

unpack_files()
make_shortcut()
success_msg()
sys.exit(1)