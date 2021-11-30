# This script asks you for a hash method to use and a string,
# then outputs the resulting hash.

# Made by Maxim Bardin with the generous help from his #python buddies at freenode.net
# Released under the GPLv3 License
# Made and tested with Python 3

# This script is meant for learning purposes, thus heavily commented.

# we need the hashlib library to use the hash methods
import hashlib

# A list of avialable hash methods
method_list="Please select your hash method: \n1) md5sum \n2) sha256 \n3) sha512 "

# setting the starting choice to zero to start the program
choice=0
# while user didn't press 1, 2 or 3 continue with the script
while choice not in ('1', '2', '3'):
    # printing our method list
    print(method_list)
    # asks the user for input
    choice=input("Press a number between 1-3 to choose: ")
    # if user chose "1" then...
    if choice == "1":
        # notifing the user of his selection
        print("You selected md5sum ")
        # asking the user for input string to hash and storing it in a var
        words=input("please write a string that you want to hash: ")
        # now all the hashing magic happens:
        # using hashlib library . hash method ((converting the input to a string)
        # encoding it with utf-8)) .using hexdigest() and storing to a new s1 var
        s1=hashlib.md5(str(words).encode('utf-8')).hexdigest()
        # now we print the output hash
        print("Your hash is: \n"+s1)
    # If the user chose 2 then run this:
    else:
        if choice == "2":
            print("You selected sha256")
            words=input("please write a string that you want to hash: ")
            s2=hashlib.sha256(str(words).encode('utf-8')).hexdigest()
            print("Your hash is: \n"+s2)
        else:
            if choice == "3":
                print("You selected sha512")
                words=input("please write a string that you want to hash: ")
                s3=hashlib.sha512(str(words).encode('utf-8')).hexdigest()
                print("Your hash is: \n"+s3)
