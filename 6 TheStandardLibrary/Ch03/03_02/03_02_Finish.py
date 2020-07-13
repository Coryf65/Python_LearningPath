import os

os.system('') # makes the color magic happen

# some Colors
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m' # to reset the console on multiple runs
    PURPLE = '\033[35m'

def find_color(user_color):
    if user_color.upper() == 'BLACK':
        return style.BLACK + user_color

    elif user_color.upper() == 'RED':
        return style.RED + user_color

    elif user_color.upper() == 'GREEN':
        return style.GREEN + user_color

    elif user_color.upper() == 'YELLOW':
        return style.YELLOW + user_color

    elif user_color.upper() == 'BLUE':
        return style.BLUE + user_color

    elif user_color.upper() == 'MAGENTA':
        return style.MAGENTA + user_color

    elif user_color.upper() == 'CYAN':
        return style.CYAN + user_color

    elif user_color.upper() == 'PURPLE':
        return style.PURPLE + user_color + ' This is mine too!'

    else:
        return f'{user_color} is not fun ... umm... {style.PURPLE} here is mine '

# Clearing the color
print(style.WHITE)

# Output, printing to the console for the user
print("Hello.")

# Input, collecting user input
color = input("What is your favorite color?")

print(find_color(color))