#!/bin/bash

# Gets file path to parent directory
FILE_PATH=$(readlink -f "${BASH_SOURCE[0]}")
CD=$(dirname "$FILE_PATH")

RANDOMWORDS_ERROR=1

python3 -m pip install RandomWords || RANDOMWORDS_ERROR=0

# Confirms that all the packages were installed
if [ $RANDOMWORDS_ERROR == 0 ]
then
  echo "Sorry. Something went wrong. You will have to install package 'RandomWords' manually."
  # Writes to the json file to tell the main script that there was an error
  echo 1 > "$CD/all_packages_installed.json"
fi

exit
