# Files and File Writing

# setting my file and pathing
my_path = 'c:/Users/Cory/Documents/_Code/Python_LearningPath/6 TheStandardLibrary/Ch03/03_03/'
test_file = 'scores.txt'

# Open a file
myFile = open(my_path + test_file, "w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print("filename " + myFile.name)
print("file Mode " + myFile.mode)

# Write to a file
print('writing to our file...')
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89") # this will overwrite all contents, we could use append mode to add onto the end
myFile.close()

# Read the file
myFile = open(my_path + test_file, "r") # we overwrote the same var because we dont need the previous data
print("Reading...\n" + myFile.read(10)) # only reading 10 chars
print("Reading again...\n" + myFile.read(10)) # only reading 10 chars, this will read the next 10 chars, due to the seek pointer