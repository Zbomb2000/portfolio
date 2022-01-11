#!/bin/bash

# Gets file path to parent directory
FILE_PATH=$(readlink -f "${BASH_SOURCE[0]}")
CD=$(dirname "$FILE_PATH")

TK_ERROR=1
SCROT_ERROR=1

sudo apt install python3-tk || TK_ERROR=0
sudo apt install scrot || SCROT_ERROR=1

# Confirms that all the packages were installed
if [ $TK_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'tkinter' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

# Confirms that all the packages were installed
if [ $SCROT_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'scrot' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

exit
