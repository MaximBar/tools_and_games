
# Made by Maxim Bardin with the generous help from his #python buddies at freenode.net
# Released under the GPLv3 License
# Made and tested with Python 3

# This script is meant for learning purposes, thus heavily commented.

# This program will generate a random password based on user's choices.

# Note that currently this script has a "bug", it won't repeat letters,numbers or symbols so:
# 1. all characters will be unique
# 2. the sum of the characters cannot be bigger than user's choice
# example, if user chooses 1 (lowercase abc), than the number of passwrd's characters
# cannot be greater than 26
# To correct this "bug" ,a different method is needed

# we need the random library
import random

# We need to define some vars so later the user can choose which combination he wants
#lowercase letters
letters=str("abcdefghijklmnopqrstuvwxyz")

# uppercase letters (we convert the last var to uppercase)
letters_upper=str(letters.upper())

#numbers
numbers=str("1234567890")

#symbols
symbols=str("~!@#$%^&*()_-+[]{}:|<>?")

# we reset the future vars for the while loop
passlen=0
comptype=0
comptype_str=0
# we create a while loop to force the user to type a number that is integer
# the passlen var will be used to define the password's lenght, so it must be an integer number
while True:
    try:
        #user's input is checked against an integer
        passlen=int(input("How many characters do you want? "))
    # if it's not an integer will print "Please type a number" and restart the loop
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
# here we force the user to type 1,2,3 or 4
while comptype_str not in ["1","2","3","4"]:
            # we display a message with the choices and ask for user's input
            comptype_str=input("What type of password do you want? \n 1) Lowercase \n 2) Lowercase+Uppercase \n 3) Lowercase+Uppercase+Numbers \n 4) Lowercase+Uppercase+Numbers+Symbols \n ")
# we convert user's input to an integer so we can evaluate it, there is also a way to do it with strings
comptype=int(comptype_str)

# here we use the vars we defined earlier mixed with user defined vars
# and using the random library to mix it up
if comptype==1:
    # if user typed 1 then password is lowercase
    password = "".join(random.sample(letters,passlen ))
elif comptype==2:
    # if user typed 2 then password is lowercase  and uppercase
    password = "".join(random.sample(letters+letters_upper,passlen ))
elif comptype==3:
    # if user typed 3 then passowrd is lowercase, uppercase and numbers
    password = "".join(random.sample(letters+letters_upper+numbers,passlen ))
elif comptype==4:
    # if user typed 4 then password is lowercase, uppercase, numbers and symbols
    password = "".join(random.sample(letters+letters_upper+numbers+symbols,passlen ))

# we display a message with the password
print("Your password is: " + "\n" + password)
