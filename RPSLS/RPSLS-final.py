#importing Modules for the Requirement

import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageDraw, ImageFont,ImageTk
import PIL.Image

# To create a GUI Window

root=Tk()
root.geometry("800x400")
root.title("Rock, Papers, Scissors, Lizard, Spock Game")
img = PIL.Image.open("RPSLS_image.jpeg")
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.image = img
panel.place(x=500,y=20)

# For Labelling

def sel():
   selection = "You selected : " + str(number_to_name(var.get()-1))
   global test
   test = var.get()-1
   global option
   option =  str(number_to_name(var.get()-1))
   label.config(text = selection)
var = IntVar()
R1 = Radiobutton(root, text="Rock", variable=var, value=1,command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Spock", variable=var, value=2,command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Paper", variable=var, value=3,command=sel)
R3.pack( anchor = W)
R4 = Radiobutton(root, text="Lizard", variable=var, value=4,command=sel)
R4.pack( anchor = W)
R5 = Radiobutton(root, text="Scissors", variable=var, value=5,command=sel)
R5.pack( anchor = W)
label = Label(root)
label.pack()

# function to convert number to name

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error"

# function to convert name to number

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print(name + "is not a character in RPSLS")

# function which selects the winner

def rpsls(guess): 
    
    # convert name to player_number using name_to_number
    player_number = name_to_number(guess)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # compute difference of player_number and comp_number modulo five
    winner = (comp_number - player_number) % 5

    # use if/elif/else to determine winner
    if winner < 3:
        player_win = False
    else:
        player_win = True
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
                   
    print("*****Player chooses " + guess+"*****")
    print ("*****Computer chooses " + comp_name+"*****")
    def win():
        if player_win:
            return ("**Player wins!**\n")
        elif comp_number == player_number:
            return ("**Player and computer tie!**\n")
        else:
            return ("**Computer wins!**\n")
    mb.showinfo("Rock,Paper,Scissors Game","**Player chooses - " + guess+"**\n"+"**Computer chooses - " + comp_name+"**\n"+win())
#For More Radio Buttons Submission
    
def submit():
    rpsls(option)
        
b1 = tk.Button(root,text = "Submit",state=ACTIVE,command = submit,activeforeground = "red",activebackground = "pink").place(x=80,y=150)
b2 = tk.Button(root,text = "Exit",state=ACTIVE,command = exit,activeforeground = "red",activebackground = "pink").place(x=160,y=150)
root.mainloop()
