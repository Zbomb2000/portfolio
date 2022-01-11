import random
import pyautogui as pygui
import os
currentDirectory = os.getcwd()
f = open(currentDirectory+'/SaveFiles/GTN.txt', 'r')
fileSave = f.read()
loseScore = float(fileSave)
f.close()

print("")
print("Starting game...")
pygui.alert("Welcome to Guess the Number!", button="Next")
while True:
    pygui.alert("You have 3 tries.", button="Next")

    numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    tries = 3
    number = random.choice(numList)
    
    while True:
        guess = pygui.prompt("Guess a number 1-10.")
        if guess == number:
            pygui.alert("YOU GUESSED THE NUMBER!!!")
            break
        elif float(guess) > float(number):
            pygui.alert("Nope! Too high!")
            tries -= 1
        elif float(guess) < float(number):
            pygui.alert("Nope! Too low!")
            tries -= 1
        else:
            pygui.alert("Please enter a number.")
        if tries == 0:
            pygui.alert("You ran out of tries. The number was "+number+". Game over.")
            loseScore += 1
            f = open(currentDirectory+'/SaveFiles/GTN.txt', 'w')
            f.write(str(loseScore))
            pygui.alert("You have lost a total of "+str(loseScore)+" times.")
            f.close()
            break
    answer = input("Enter 1 to play again, or enter anything else to leave: ")
    if answer != '1':
        break
print("Thank you for playing!")
print("")
