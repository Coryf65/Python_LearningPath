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
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open(my_path + test_file, "r")
print("Reading..." + myFile.read(10))

# closing and reopening we are resetting our seek pointer so we start at the begining
myFile.close() 
myFile = open(my_path + test_file, "r")

# Reading from the start again
print("Reading again" + myFile.read(10))