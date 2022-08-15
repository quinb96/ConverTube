def make_shortcut():
    if sys.platform == "linux" or sys.platform == "linux2":
        shortcutinfo = """[Desktop Entry]
Name=ConverTube
Version=1.0
Icon=/home/quin/.local/ConverTube/assets/CT_app_icon.ico
Exec=python3 /home/quin/.local/ConverTube/ConverTube.py
Terminal=False
Type=Application"""
        with open("/home/quin/.local/share/applications/ConverTube.desktop", "w") as desktopshortcutwriter:
            desktopshortcutwriter.write(shortcutinfo)
        desktopshortcutwriter.close()
    elif sys.platform == "win32":
        #No process for Windows yet
        print("Windows OS detected from make_shortcut()!")
        #Make function that copies packages to ~/Program_Files(x86)