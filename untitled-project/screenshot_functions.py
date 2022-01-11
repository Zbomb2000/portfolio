#!/usr/bin/python3

# [NOTE] The eval method it tagged out, as it is not in use right now
# -------------------------------------------------------------------------------------------
# WARNING: DO NOT MESS WITH THIS FILE
# This file uses the "eval" method
# Messing with this file then using the program could possibly destroy your operating system
# YOU HAVE BEEN WARNED.
# -------------------------------------------------------------------------------------------

import pyautogui as pygui
import os
import sys
import json
import pytesseract
import cv2
from PIL import Image
from datetime import datetime as dt
import platform

# This gets the current working directory from file path files
file_directory = os.path.dirname(__file__)
file = open(file_directory + r"/ef_file_path.json")
cd_var = json.load(file)
cd = r"{}".format(cd_var)
file.close()

# Imports error functions
sys.path.insert(1, cd + '/external-functions/other')
from error_messages import Error
sys.path.insert(1, cd + '/external-functions')


# Function to take a screenshot
def takeScreenshot():
    # This gets the current working directory from file path files
    file_directory = os.path.dirname(__file__)
    file = open(file_directory + r"/ef_file_path.json")
    cd_var = json.load(file)
    cd = r"{}".format(cd_var)
    file.close()

    # Takes screenshot
    ss = pygui.screenshot()

    # Saves screenshot
    ss.save("Screenshot.png")
    # Moves screenshot to 'screenshot'
    os.replace("Screenshot.png", cd + "/data/screenshot/Screenshot.png")
    return 'Done!'


def scanScreenshot():
    # This gets the current working directory from file path files
    file_directory = os.path.dirname(__file__)
    file = open(file_directory + r"/ef_file_path.json")
    cd_var = json.load(file)
    cd = r"{}".format(cd_var)
    file.close()

    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Loads and scans the image
    ss_text_raw = pytesseract.image_to_string(Image.open(cd + r"/data/screenshot/Screenshot.png"))

    # Makes sure there are no 'os.system' functions that got read instead of an equation
    if "os.system" in ss_text_raw:
        pygui.alert(
            "The text scanned contains an 'os.system()' function.\nIf possible, please send the screenshot in the '/data/screenshot' folder to 'hxl9500@gmail.com' with the subject 'FATAL ERROR (os.system.)'.\nAlso, please send the '/error_log.txt' file along with the screenshot.")
        Error.logError("FATAL", "50", "OS.SYSTEM_ERROR", "/external-functions/scanscreenshot.py", "scanScreenshot")
        print("[FATAL ERROR] Program exiting...")
        sys.exit()
    elif "sys" in ss_text_raw:
        pygui.alert(
            "Our program detected a 'sys' function in the text.\nIf possible, please send the screenshot in the '/data/screenshot' folder to 'hxl9500@gmail.com' with the subject 'FATAL ERROR (sys)'.\nAlso, please send the '/error_log.txt' file along with the screenshot.")
        Error.logError("FATAL", "50", "SYS ERROR", "/external-functions/screenshot_functions.py", "scanScreenshot")
        print("[FATAL ERROR] Program exiting...")
        sys.exit()

    return ss_text_raw


# noinspection PyUnusedLocal
def processScreenshot(ssdata):
    # This function writes errors to the log file
    # def Error.logError(error_level, error_code, error_name, script_path, function_name):
    #    print("[INFO] Writing to log file...")
    #    with open(cd + r"/error_log.txt", 'a') as f:
    #        date = str(dt.now())
    #        f.write(
    #            "\n" + date + " - " + error_level + ": CODE " + error_code + ": '" + error_name + "''. SCRIPT_PATH: '" + script_path + "' FUNCTION_NAME: '" + function_name + "'")
    #    print("[INFO] Done!")
    #    print()

    # WARNING: THIS FUNCTION USES THE EVAL METHOD
    # The variable 'ssdata' should be already scanned and safe to use here
    # If you somehow edited the ssdata variable, you could possibly break your operating system
    # YOU HAVE BEEN WARNED (again)

    # This solves the problem with the 'eval' method
    # finisheddata = eval(ssdata)

    # This makes sure the answer is a number
    # for i in input.split():
    #   if i not in ['+', '-', '*', '%', '.'] and not i.isdigit():
    #       print("[ERROR] The 'screenshotdata' variable isn't a number. Exiting program...")
    #       Error.logError("MODERATE", "100", "SCREENSHOTdata_VAR ERROR", "/external-functions/scanscreenshot.py", "processScreenshot")
    #       sys.exit()

    # pygui.alert("The answer to the equation is '" + finisheddata + "'.")

    Error.visualError("[ERROR]\nIt seems that this part of the program is not finished. When it is finished, this will do something besides make a popup box telling you that this isn't finished.")

    print("[INFO] Printed answer")
    print()
