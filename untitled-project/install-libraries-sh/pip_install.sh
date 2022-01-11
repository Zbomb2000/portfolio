#!/bin/bash

# Gets file path to parent directory
FILE_PATH=$(readlink -f "${BASH_SOURCE[0]}")
CD=$(dirname "$FILE_PATH")

PIP_ERROR=1

# Installs pip3 if it hasn't already been installed
sudo apt install python3-pip || PIP_ERROR=0

# Confirms that all the packages were installed
if [ $PIP_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'python3-pip3' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

exit
