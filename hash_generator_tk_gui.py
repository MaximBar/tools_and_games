# This script takes an input file from the user and a hash method,
# then prints the hash to text window and the command line

# Made by Maxim Bardin with the generous help from his #python buddies at freenode.net
# Released under the GPLv3 License
# Made and tested with Python 3

# This script is meant for learning purposes, thus heavily commented.


import hashlib
import tkinter

# next script, try using pyqt5

# importing askopenfilename for the browse button
from tkinter.filedialog import askopenfilename

# To use the Tkinter text widget we need to import all:
from tkinter import *

# we need to create functions in order to use them in buttons:
# a browse button function that opens the browse window
def browse():
    global infile #need to make it global to use it later
    infile=askopenfilename() # opens a browse window

# defining md5sum function
def md5sum():
    # Takes the input file and hashes
    s1=hashlib.md5(str(infile).encode('utf-8')).hexdigest()
    T.delete(1.0,END) # deletes the current content in the window
    T.insert(END, s1) # inserts the hash to the window
    print("Your hash is: \n"+s1) # also prints the hash to the command line

def sha256():
    s2=hashlib.sha256(str(infile).encode('utf-8')).hexdigest()
    T.delete(1.0,END)
    T.insert(END, s2)
    print("Your hash is: \n"+s2)

def sha512():
    s3=hashlib.sha512(str(infile).encode('utf-8')).hexdigest()
    T.delete(1.0,END)
    T.insert(END, s3)
    print("Your hash is: \n"+s3)

#def hash_out():
#T.insert(END, "Just a text Widget\nin two lines\n")

root1=tkinter.Tk() #creates an empty window
root1.title("Hash Generator") # creates a title of the window
# creating a label, a main text:
label=tkinter.Label(root1,text="This program generates hash from a file")
# to use it, we need to pack it:
label.pack()
# creating browse button
browseButton=tkinter.Button(root1,text="Browse",command=browse) #we can add ,command=Function
browseButton.pack()

#we are also calling the function we created upun pressing the button
md5sum_button=tkinter.Button(root1,text="Generate md5sum",command=md5sum)
md5sum_button.pack()

sha256_button=tkinter.Button(root1,text="Generate sha256",command=sha256)
sha256_button.pack()

sha512_button=tkinter.Button(root1,text="Generate sha512",command=sha512)
sha512_button.pack()


T=Text(root1, height=6, width=50)
T.pack()

# T.insert(END, "Just a text Widget\nin two lines\n")

# keeps the window on the screen until user closes it
# it also closes the loop!
# so all code of the window needs to end before this command
root1.mainloop()
