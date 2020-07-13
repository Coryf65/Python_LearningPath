# HTML Parser Module

from html.parser import HTMLParser

# setting my file and pathing
my_path = 'c:/Users/Cory/Documents/_Code/Python_LearningPath/6 TheStandardLibrary/Ch04/04_05/'
html_file = 'sampleHTML.html'

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr:", attr)
    def handle_endtag(self, tag):
        print("End tag: ", tag)
    def handle_comment(self, data):
        print("Comment: ", data)
    def handle_data(self, data):
        print("Data: ", data)

parser = Parser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>")
print() # prints an empty line

input = input("Put in HTML Code")
parser.feed(input)
print() # prints an empty line

htmlFile = open(my_path + html_file, "r")
s = "" # this holds our each line of the file to feed for the parser
for line in htmlFile:
    s += line
parser.feed(s)