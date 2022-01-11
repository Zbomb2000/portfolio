#!/bin/bash

# Gets file path to parent directory
FILE_PATH=$(readlink -f "${BASH_SOURCE[0]}")
CD=$(dirname "$FILE_PATH")

PILLOW_ERROR=1

python3 -m pip install pillow && sudo apt install python3-pil python3-pil.imagetk || PILLOW_ERROR=0

# Confirms that all the packages were installed
if [ $PILLOW_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'pillow' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

exit
