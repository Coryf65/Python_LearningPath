#!/usr/bin/python3
# label.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
import os

cwd = os.path.dirname(os.path.abspath(__file__)) # path to this current files dir

root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text = 'Howdy, Tkinter!')
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
label.config(wraplength = 150) # num of pixels
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = 'Howdy, Tkinter!')

logo = PhotoImage(file = f'{cwd}/python_logo.gif') # change path to image as necessary
label.config(image = logo) # does not save a reference to the image
label.config(compound = 'text')
label.config(compound = 'center') # displays text over the image
label.config(compound = 'left') # image left of the text

# always store the image, creating a img object in the label
label.img = logo
label.config(image = label.img) # tell label to use this image

root.mainloop()
