# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import json
import textwrap

# using google books API, we are pulling a GET request
with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f: # if this runs we create it as a var f
    text = f.read() 
    decodedtext = text.decode('utf-8') # this is decoded so we can print it out
    print(textwrap.fill(decodedtext, width=50)) # some formatting

print() # new line

# this API returns a JSON object, Going to the link we can see this
obj = json.loads(decodedtext)
# if we look at the JSON return info we can see a Key, 'kind'
print(obj['kind'])
# getting some diff info
print(obj['items'][0]['searchInfo']['textSnippet']) # 0 is there for the list accessing the List[0], first item