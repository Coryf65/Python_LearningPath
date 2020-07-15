#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk # these are themed widgets

root = Tk()

# each tkinter widget is a class
button = ttk.Button(root, text = 'Click Me') # this creates the button
button.pack() # this loads into into view

print(button['text']) # current value
button['text'] = 'Press Me' # assign the new text value
button.config(text = 'Push Me') # we can also call this to change props
print(button.config()) # returns a DICT() with all props related to this widget and their values

print(str(button)) # returns the underlying tk name
print(str(root)) # top level name '.'

ttk.Label(root, text ='Hello, Tkinter!').pack() # you can create a label without storing the data, but we couldn't access this programmatically later

# mainloop() add
root.mainloop()
