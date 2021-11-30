# Rock Paper Scissors
# This is a Rock Paper Scissors game, it asks the user for input, assignes vars
# And calculates the result

# Made by Maxim Bardin with the generous help from his #python buddies at freenode.net
# Released under the GPLv3 License
# Made and tested with Python 3

# This script is meant for learning purposes, thus heavily commented.

# First we import the random library for the program to be able
# to randomly choose between the given options 1, 2 or 3
import random
# Program choices:
comp=random.choice([1,2,3])

# we set the user var to 0, to make a while loop
user=0
# we want the loop so if user chooses a different letter,
# the program will re-run
while user not in ["r","p","s"]:
    # printing welcome message
    print("Welcome To The Rock, Paper, Scissors Game!")
    # printing message to the user, waiting for his input
    # and assigning the value to "user"
    user=input("Please pick Rock(r), Paper(p) or Scissors(s) ")
    # user choices:
    if user=="r":
        # if user typed "r", assign the value "Rock" to var "u", and print a message
        print("You picked Rock")
        u="Rock"
        #print(u)
    elif user=="p":
        # else, if user typed "p", assign the value "Paper" to var "u", and print a message
        print("You picked Paper")
        u="Paper"
        #print(u)
    elif user=="s":
        # # else, if user typed "s", assign the value "Scissors" to var "u", and print a message
        print("You picked Scissors")
        u="Scissors"
        #print(u)
    else:
        # if user typed something else, print this message
        # (the script will go back to user input)
        print("Please type 'r', 'p' or 's' ")

# Computer choices from the random.choice([1,2,3]) command
if comp==1:
    # if computer randomy picked "1", assign com the value of "Rock", and print a message
    print("Computer played Rock")
    com="Rock"
elif comp==2:
    # if computer randomy picked "2", assign com the value of "Paper", and print a message
    print("Computer played Paper")
    com="Paper"
elif comp==3:
    # if computer randomy picked "3", assign com the value of "Scissors", and print a message
    print("Computer played Scissors")
    com="Scissors"

# the battle
# now we manually "compare" values,
# as strings cannot be automatically compared, "ADX" is not comparable to "HGA",
# we need to create if statments

# If user chose "Rock"
if u == "Rock":
    # and computer chose "Rock", print "Draw"
    if com=="Rock":
        print("Draw")
    # else if computer chose "Paper", print "Computer Won"
    elif com=="Paper":
        print("Computer Won")
    # else if computer chose "Scissors", print "User won"
    elif com=="Scissors":
        print("User won")

# same logic as above
if u == "Paper":
    if com=="Rock":
        print("User Won")
    elif com=="Paper":
        print("Draw")
    elif com=="Scissors":
        print("Computer Won")

# same logic as above
if u == "Scissors":
    if com=="Rock":
        print("Computer Won")
    elif com=="Paper":
        print("User Won")
    elif com=="Scissors":
        print("Draw")
