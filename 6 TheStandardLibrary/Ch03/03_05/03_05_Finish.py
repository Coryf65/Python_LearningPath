# Iterative Files

# setting my file and pathing
my_path = 'c:/Users/Cory/Documents/_Code/Python_LearningPath/6 TheStandardLibrary/Ch03/03_03/'
test_file = 'scores.txt'

# reading the file one line at a time
myFile = open(my_path + test_file, "r")

# Read one line at a time
print("My one line: " + myFile.readline())
myFile.seek(0) # resetting the seek at the start

# Iterate through each line of a file
for line in myFile:
    # here we are replacing some data with a new value
    # we did not replace the data in the file but our value that we hold in our string
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer)

# closing the file
myFile.close()