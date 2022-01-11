#!/usr/bin/python3

import pyautogui as pygui
from random_words import RandomNicknames
import string
import random

# This is for error messages
class Error:
    # This writes an error to the log file
    @staticmethod
    def logError(error_level, error_code, error_name, script_path, function_name):
        print("[INFO] Writing to log file...")
        # Writes error to log file
        with open(cd + r"/error_log.txt", 'a') as f:
            # Gets current date
            date = str(dt.now())
            f.write("\n" + date + " - " + error_level + ": CODE " + error_code + ": '" + error_name + "''. SCRIPT_PATH: '" + script_path + "' FUNCTION_NAME: '" + function_name + "'")
        print("[INFO] Done!")
        print()

    # This makes a message box with the error description in it
    @staticmethod
    def visualError(message):
        # Adds a random name to the message box
        rn = RandomNicknames()
        abc_list = list(string.ascii_lowercase)
        random_name_var = rn.random_nick(random.choice(abc_list), 'u')
        # Sends message box
        pygui.alert(message + "\n\nIn the meantime, here's a random name: '" + random_name_var + "'")
