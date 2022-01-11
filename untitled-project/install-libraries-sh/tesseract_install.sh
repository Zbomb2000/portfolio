#!/bin/bash

# Gets file path to parent directory
FILE_PATH=$(readlink -f "${BASH_SOURCE[0]}")
CD=$(dirname "$FILE_PATH")

TESSERACT_OCR_ERROR=1
PYTESSERACT_ERROR=1

# Installs stuff for tesseract ocr
sudo apt install tesseract-ocr || TESSERACT_OCR_ERROR=0

# Installs pytesseract
python3 -m pip install pytesseract || PYTESSERACT_ERROR=0

# Confirms that all the packages were installed
if [ $TESSERACT_OCR_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'tesseract ocr' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

if [ $PYTESSERACT_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'pytesseract' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

exit
