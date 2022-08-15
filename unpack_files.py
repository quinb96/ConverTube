def path_checker():
    print("Application is already installed.\nExiting setup script...")

def unpack_files():
    #Function will check if device is Windows.
    #If it is, copy app files to ~/Program_Files(x86)
    if sys.platform == "linux" or sys.platform == "linux2":
        try:
            shutil.copytree("../ConverTube", os.path.expanduser("/home/quin/.local/ConverTube")) #Unpacking files
        except IOError:
            #If the folder was written
            if os.path.exists("/home/quin/.local/ConverTube"):
                path_checker()
                sys.exit(1) #Exit setup script
            else:
                pass #Otherwise, do nothing
    elif sys.platform == "win32":
        print("Windows OS detected from unpack_files()!")