#!/usr/bin/python3

#prototype of a gui based tool to mass-watermark images
#using tkinter and pillow.
#still in early conceptual phase

from tkinter import *
from os import path
import time

#setting up
root = Tk()
root.title("Bulk Watermark")
localtime = time.asctime(time.localtime(time.time()))

#define elements
timelabel = Label(root, text = localtime)
nlabel = Label(root, text = "Name")
plabel = Label(root, text = "Webauftritt")

nentry = Entry(root)
pentry = Entry(root)

cb = Checkbutton(root, text = "Auf allen Bildern anwenden")

dir_btn = Button(root, text = "Durchsuchen")
dir_path = Entry(root)
start_btn = Button(root, text = "Stempeln")
exit_btn = Button(root, text = "Beenden")

#functions
def leftClickDirBtn(event):
    print("Durchsuchen")
    #place code for browsing directories in here
    #right now it just uses a dummy-function, pls remove or
    #comment out the print statement

def leftClickStmpBtn(event):
    print("Stempeln")
    #place code for setting a watermark
    #pls remove print statement

def leftClickExBtn(event):
    print("Beenden")
    root.quit()

#bind functions to buttons
dir_btn.bind("<Button-1>", leftClickDirBtn)
start_btn.bind("<Button-1>", leftClickStmpBtn)
exit_btn.bind("<Button-1>", leftClickExBtn)

#placement
nlabel.grid(row = 0, sticky = E)
plabel.grid(row = 1, sticky = E)

nentry.grid(row = 0, column = 1)
pentry.grid(row = 1, column = 1)

cb.grid(columnspan = 2)

dir_btn.grid(row = 3, sticky = E)
dir_path.grid(row = 3, column = 1)
start_btn.grid(columnspan = 2)
exit_btn.grid(columnspan = 2)
timelabel.grid(columnspan = 2)

#call that shit up
root.mainloop()
