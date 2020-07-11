""" The Hierarchy of Packages """

import urllib.request

# retrieve google.com home page
print(urllib.request.urlopen('https://www.google.com'))

# get the path to urllib package, points to the folder that contains the module
print(urllib.__path__)
