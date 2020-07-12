""" Trying to Download Things That Don't Exist """

import urllib.request

# if we lost internet then we would get an error
# now we can use some simple error handling
try:
    webpage = urllib.request.urlopen('http://www.google.com')    
except:
    print('Could not reach website..')
else:
    # this else will only run if try is a success
    for line in webpage:
        print(line)
