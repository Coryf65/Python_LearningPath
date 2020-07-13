# Zipfile Module
import zipfile

# setting my file and pathing
my_path = 'c:/Users/Cory/Documents/_Code/Python_LearningPath/6 TheStandardLibrary/Ch03/03_07/'
zip_file = 'Archive.zip'

# Open and List, looking into our Zip File
zip = zipfile.ZipFile(my_path + zip_file, 'r')
# printing all into a list
print(zip.namelist())

# Metadata in the zip folder, this displays the metadata about each file in the archive
for meta in zip.infolist():
    print(meta)

print('\nGetting a specific file data')
info = zip.getinfo("purchased.txt")
print(info)

# Access to files in zip folder, a quick and dirty read!
print('\nReading the wishlist file')
print(zip.read("wishlist.txt"))

# we can also read this way, but we get more access to the file this way!
# if this opens the txt file okay read it
# we could do lots more by opening a file this way!
with zip.open('wishlist.txt') as f:
    print(f.read())

# Extracting files
#zip.extract("purchased.txt")
zip.extractall(my_path)

# Closing the zip
zip.close()

