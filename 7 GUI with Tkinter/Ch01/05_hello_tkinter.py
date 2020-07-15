#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *

# constructor
root = Tk()

# create a label and pack to ad dinto our window
Label(root, text="Hello, Tkinter!").pack()
root.mainloop()
