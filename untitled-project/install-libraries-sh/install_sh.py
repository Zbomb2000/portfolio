#!/usr/share/python3

import json
import os
import subprocess
import sys
import stat

def linuxInstall(cd_var, libraries):
    # Gets all file paths for install files
    with open(cd_var+r"/_data/_other/install_file_paths.json") as file:
        install_file_paths = json.load(file)

    # Clears terminal
    os.system('clear')

    # Runs scripts if needed
    if "  - pyautogui (python3 -m pip install pyautogui)" in libraries:
        subprocess.call([cd_var + install_file_paths["pyautogui_install"]])

    if "  - pytesseract (python3 -m pip install pytesseract)" in libraries:
        subprocess.call([cd_var + install_file_paths["tesseract_install"]])

    if "  - pillow (python3 -m pip install pillow)" in libraries:
        subprocess.call([cd_var + install_file_paths["pillow_install"]])

    if "  - cv2 (python3 -m pip install opencv-python)" in libraries:
        subprocess.call([cd_var + install_file_paths["cv2_install"]])

    if "  - tkinter (python3 -m pip install python3-tk)" in libraries:
        subprocess.call([cd_var + install_file_paths["tkinter_install"]])

    if "  - random_words (python3 -m pip install RandomWords)" in libraries:
        subprocess.call([cd_var + install_file_paths["randomwords_install"]])

    # Runs apt update and upgrade
    subprocess.call([cd_var + r"/_external_functions/_other/_install_libraries_sh/update.sh"])

    # Sees if all the packages were installed successfully
    with open(cd_var + r"/_external_functions/_other/_install_libraries_sh/all_packages_installed.json", 'r') as read_file:
        all_packages_installed = json.load(read_file)

    # Checks to see if all the packages were installed
    if all_packages_installed == 0:
        print()
        print()
        print("All packages were successfully installed! Please run 'Main.py' again for the addition to take effect.")
        print()
        print("[EXIT] Exiting program...")
        print()
        sys.exit()
    else:
        print("Sorry, something went wrong. All/Some of the packages were not installed.")
        print()
        print("[EXIT] Exiting program...")
        print()
        sys.exit()

def windowsInstall(cd_var):
    # Clears terminal
    os.system('cls')
    # Runs script
    subprocess.call([cd_var + r'/_external_functions/_other/install_all=_libraries_py3_windows.bat'])
    # Sees if all the packages were installed successfully
    with open(cd_var + r"/_external_functions/_other/all_packages_installed.json", 'r') as read_file:
        all_packages_installed = json.load(read_file)
    # Checks to see if all the packages were installed
    if all_packages_installed == 1:
        print()
        # Checks to see if tkinter is installed because I can't install it with pip
        if tkinter_error:
            print("It seems that you don't have the package 'tkinter' installed.")
            print("You will need to find a way to manually install it.")
            # Writes that all the packages weren't installed
            with open(cd_var + r"/_external_functions/_other/all_packages_installed.json", 'w') as write_file:
                json.dump(0, write_file)
            time.sleep(5)
            print()
            print("[EXIT] Exiting program...")
            print()
            sys.exit()
        else:
            # Runs if all the packages were installed successfully
            print("All packages were successfully installed! Please run 'Main.py' again for the addition to take effect.")
            print()
            print("[EXIT] Exiting program...")
            print()
            time.sleep(3)
            sys.exit()
    else:
        # Runs if some or all of the packages weren't installed correctly
        print()
        print("Sorry, something went wrong. All/Some of the packages were not installed. You will have to install those packages manually.")
        print()
        print("[EXIT] Exiting program...")
        print()
        time.sleep(5)
        sys.exit()
