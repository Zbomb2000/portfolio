#!/usr/bin/python3

# Importing modules
print("[PROGRAM] Importing modules...")

import subprocess
import sys
import os
import platform
import json
import stat
import time
from multiprocessing import Process

# These variables are used to see what libraries are or aren't installed
cv2_error = False
pygui_error = False
pytesseract_error = False
tkinter_error = False
pillow_error = False
colorama_error = False
randomName_error = False

# noinspection PyBroadException
try:
    from colorama import Fore, Back
except:
    print()
    print("ERROR: You need to install the following libraries:")
    print(" - colorama (python3 -m pip install colorama)")
    print("Attempting to auto-install...")
    print()
    try:
        os.system('python3 -m pip install colorama')
        print("'colorama' was successfully installed! Please relaunch the program for the changes to take effect")
        print()
        print("IMPORTANT: If it says 'attempt failed', this is an error that I can't figure out how to fix.")
        print()
        print("[EXIT] Exiting program...")
        print()
        time.sleep(2)
        sys.exit()
    except:
        print()
        print("Attempt failed. You will have to install 'colorama' manually.")
        print()
        print("[EXIT] Exiting program...")
        print()
        time.sleep(2)
        sys.exit()


# This gets the current working directory from file path files
def getCdVar():
    cd = os.path.dirname(__file__)
    raw_cd_var = r"{}".format(cd)

    # Prints the 'untitled_project-Bot' file path
    print()
    print("[NOTE] The file path to 'untitled_project-Bot' is '" + cd + "'")
    print()

    # Writes the file path to all the file path files
    with open(cd + r"/data/data_file_path.json", 'w') as dump_file:
        json.dump(cd, dump_file)
    with open(cd + r"/external-functions/ef_file_path.json", 'w') as dump_file:
        json.dump(cd, dump_file)
    with open(cd + r"/path.json", 'w') as dump_file:
        json.dump(cd, dump_file)

    return raw_cd_var


cd_var = getCdVar()


# This confirms if the user should run in sudo mode
def confirmSudoMode():
    while True:
        sudo_confirm = pygui.confirm("Do you want to run in sudo mode or normal mode?", buttons=["SUDO", "NORMAL", "DISABLE SUDO RUN IN NORMAL", "EXIT"])
        # Start in sudo mode
        if sudo_confirm == "SUDO":
            print("[PROGRAM] Starting in SUDO MODE...")
            print()
            return True
        # Start in normal mode
        elif sudo_confirm == "NORMAL":
            print("[PROGRAM] Starting in NORMAL MODE...")
            print()
            return False
        # Disable sudo mode and start in normal mode
        elif sudo_confirm == "DISABLE SUDO RUN IN NORMAL":
            if pygui.confirm("Are you sure you want to disable sudo mode?", buttons=["YES", "NO"]) == "YES":
                print("[PROGRAM] Disabling SUDO MODE...")
                # This disables sudo mode
                with open(cd_var + r"/data/device_info.json", 'r') as f:
                    device_info_dict = json.load(f)
                    device_info_dict["admin"] = 0
                with open(cd_var + r"/data/device_info.json", 'w') as dump_file:
                    json.dump(device_info_dict, dump_file)
                print("[PROGRAM] Starting in NORMAL MODE...")
                print()
                return False
            else:
                print("[NOTE] sudo mode not disabled")
                print()
        else:
            print("[EXIT] Exiting program...")
            print()
            sys.exit()

# Checks to see if the program has been run before
def firstTimeSetup():
    with open(cd_var + r"/data/run.json", 'r') as file_thing:
        file_contents = json.load(file_thing)
        if file_contents['first_time_setup'] == 1:
            first_time_setup_in_function = False
        else:
            print("[PROGRAM] Running first time setup...")
            print()
            first_time_setup_in_function = True
    return first_time_setup_in_function


first_time_setup = firstTimeSetup()


# This is the function checks what libraries need to be installed
def libraryInstallCheck():
    libraries_that_need_installed = []

    # This prints what libraries need to be installed
    if pygui_error:
        libraries_that_need_installed.append("  - pyautogui (python3 -m pip install pyautogui)")
    if pytesseract_error:
        libraries_that_need_installed.append("  - pytesseract (python3 -m pip install pytesseract)")
    if cv2_error:
        libraries_that_need_installed.append("  - cv2 (python3 -m pip install opencv-python)")
    if pillow_error:
        libraries_that_need_installed.append("  - pillow (python3 -m pip install pillow)")
    if tkinter_error:
        libraries_that_need_installed.append("  - tkinter (Linux: 'sudo apt install python3-tk')")
    if randomName_error:
        libraries_that_need_installed.append("  - random_words (python3 -m pip install RandomWords)")

    print()
    print(Fore.RED+" ERROR: "+Fore.RESET+"You need to install the following libraries:")
    print("\n".join(libraries_that_need_installed))
    print()
    print()

    # Asks to install libraries automatically
    while True:
        print("It seems there are required libraries that are not installed.")
        # Gets input
        install_libraries_input = input("Would you like to automatically install the required libraries? (y/n): ")

        # Processes input
        if install_libraries_input.lower() == "y":
            # Runs the file that installs the libraries
            if platform.system() == "Linux":
                installLibrariesLinux(cd_var, libraries_that_need_installed)
            elif platform.system() == "Windows":
                installLibrariesWindows(cd_var, libraries_that_need_installed)
            break
        elif install_libraries_input.lower() == "n":
            # Exits the program
            print("You will need to install the libraries manually.")
            print()
            print("[EXIT] Exiting program...")
            print()
            sys.exit()
        elif install_libraries_input.lower() == "yes":
            # Runs the file that installs the libraries
            if platform.system() == "Linux":
                installLibrariesLinux(cd_var, libraries_that_need_installed)
            elif platform.system() == "Windows":
                installLibrariesWindows(cd_var, libraries_that_need_installed)
            break
        elif install_libraries_input.lower() == "no":
            # Exits the program
            print("You will need to install the libraries manually.")
            print()
            print("[EXIT] Exiting program...")
            print()
            sys.exit()
        else:
            print("Please type 'y' or 'n'.")
            print()


# This sees what libraries are or aren't installed
try:
    import pyautogui as pygui
except:
    pygui_error = True

try:
    try:
        import tkinter as tk
    except:
        import Tkinter as tk
except:
    tkinter_error = True

try:
    import PIL
    from PIL import ImageTk
except:
    pillow_error = True

# ------------------------This will probably be removed later-------------------

try:
    import cv2
except:
    cv2_error = True

try:
    import pytesseract
except:
    pytesseract_error = True

try:
    from random_words import RandomNicknames
except:
    randomName_error = True

# ------------------------------------------------------------------------------

# Import install functions
sys.path.insert(1, cd_var + "/external-functions/other/install-libraries-sh")
from install_sh import linuxInstall as installLibrariesLinux
from install_sh import windowsInstall as installLibrariesWindows
sys.path.insert(1, cd_var)

# This checks the platform of the host to send the right command to clear the terminal
if platform.system() == "Windows":
    os.system('cls')
elif platform.system() == "Linux":
    os.system('clear')

# This checks if the required libraries are installed
if pygui_error:
    libraryInstallCheck()
elif cv2_error:
    libraryInstallCheck()
elif pytesseract_error:
    libraryInstallCheck()
elif pillow_error:
    libraryInstallCheck()
elif tkinter_error:
    libraryInstallCheck()
elif randomName_error:
    libraryInstallCheck()

# This imports functions from external scripts
sys.path.insert(1, cd_var + '/external-functions')

# Imports ui functions
from main_ui import StartScreens

sys.path.insert(1, cd_var + '/external-functions/sudo-mode')
import login

sys.path.insert(1, cd_var + '/external-functions')

# Imports screenshot functions
from screenshot_functions import takeScreenshot
from screenshot_functions import scanScreenshot
from screenshot_functions import processScreenshot

# Imports error functions
sys.path.insert(1, cd_var + '/external-functions/other')
from error_messages import Error
# Imports warning email function
from send_email import sendWarningEamil
sys.path.insert(1, cd_var + '/external-functions')

# Imports other functions
from screenshot_verify import screenshotVerify

from main_ui import whatsNew

sys.path.insert(1, cd_var)

print("[PROGRAM] Finished importing libraries and external functions.")
print()


class Main:
    """This is the main class with all the functions to run the program"""

    # This runs through the screens for first time setup
    @staticmethod
    def firstTimeSetupMenus():
        start_screens = StartScreens()

        # Asks the user if they want to be running the program as admin
        start_screens.adminVerification()

        # User information screen
        start_screens.userInformation()

        # Final warning
        start_screens.finalWarning()

        # Sets first time setup as finished
        with open(cd_var + r"/data/run.json", 'r') as creative_file_variable_name:
            information = json.load(creative_file_variable_name)
            information['first_time_setup'] = 1
        with open(cd_var + r"/data/run.json", 'w') as creative_file_variable_name:
            json.dump(information, creative_file_variable_name)

    # This is a function that is used to take a screenshot
    @staticmethod
    def takeScreenshotFunction():
        direc = cd_var + "/data/screenshot"
        for f in os.listdirec(direc):
            os.remove(os.path.join(direc, f))

        takeScreenshot()
        return "Done!"

    # This runs the functions to scan and process the screenshot
    @staticmethod
    def scanScreenshotFunction():
        ss_text = scanScreenshot()
        processScreenshot(ss_text)

    @staticmethod
    def onOpenWarning():
        warning_input = pygui.confirm("[WARNING]\nUSING THIS PROGRAM IS CONSIDERED CHEATING. Do not use this unless you have extreme anxiety and/or depression from untitled_project.", buttons=["CONTINUE", "TURN BACK"])
        if warning_input is None:
            pygui.alert("Good choice.", button="EXIT")
            sys.exit()
        elif warning_input == "CONTINUE":
            pygui.alert("You have been warned...")
        elif warning_input == "TURN BACK":
            pygui.alert("Good choice.", button="EXIT")
            sys.exit()


def mainStuff():
    # This gets all the device information
    with open(cd_var + r"/data/device_info.json", 'r') as file:
        device_info = json.load(file)
        # Checks for sudo mode
        sudo_mode = device_info["admin"]

        # Gets screen resolution
        class Screen:
            x = device_info["x"]
            y = device_info["y"]

        print("[NOTE] Screen resolution is set to " + str(Screen.x) + "x" + str(Screen.y))
        print()

    # Runs in sudo mode if it is enabled
    if sudo_mode == 1:
        run_sudo = confirmSudoMode()
        if run_sudo:
            login.adminLogin(cd_var)
        elif not run_sudo:
            pass
        else:
            print("[FATAL ERROR] Somehow, something went wrong when trying to decide if sudo mode should be enabled.")
            Error.logError("FATAL", "150", "Something went wrong when starting in sudo mode", "/Main.py", "mainStuff")
            print()
            print("[EXIT] Exiting program...")
            print()
            sys.exit()

    # Prints keyboard and screenshot warning if it's the first time running.
    screenshotVerify()

    # This is where the actual script starts

    # Gets information from run.json
    with open(cd_var + r"/data/run.json", 'r') as file:
        info = json.load(file)

    if not first_time_setup:
        Main.onOpenWarning()

    # Displays what's new screen
    if info['whats_new'] == 0:
        p = Process(target=whatsNew)
        p.start()

    if first_time_setup:
        # Displays the first time setup prompts
        Main.firstTimeSetupMenus()

        # Sends warning email
        with open(cd_var+r"/data/user_information.json") as file:
            # Loads email from the json file
            email_true = json.load(file)
            if email_true['email'] != 0:
                sendWarningEamil()

    # -------ANYTHING BEYOND THIS POINT IS UNFINISHED AND IS DEFIANTLY GOING TO CHANGE--------

    # This is the main loop.
    while True:
        main_input = pygui.confirm("Please select an option.", buttons=["Scan", "Quit"])

        if main_input == "Quit":
            print("[EXIT] Exiting program...")
            print()
            sys.exit()
        elif main_input == "Scan":
            time.sleep(1)
            # Main.takeScreenshotFunction()
            # Main.scanScreenshotFunction()
            Error.visualError("[ERROR]\nThis part of the program is not finished yet. When it is finished, it will do something besides display an error and say that it's not finished.")
        elif main_input is None:
            print("[EXIT] Exiting program...")
            print()
            sys.exit()


# This runs everything in the script
if __name__ == '__main__':
    mainStuff()
