#! /bin/bash

cd /home/maritatol23/Attempt
gameChoose=$(zenity --list --title="Choose what version you want to launch." --column="Game" --column="File Type" 1 .x86_64 2 .x86_64)

if [ $gameChoose = "1" ]
then
    echo "Starting classic."
    ./BALDI.x86_64
fi
    
if [ $gameChoose = "2" ]
then
    echo "Starting other."
    ./PARTY.x86_64
fi

exit
