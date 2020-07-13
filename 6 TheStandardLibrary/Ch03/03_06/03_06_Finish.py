# Tempfile Module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b"Save this special number for me: 5678309") # this b converts this string into bytes
tempFile.seek(0) # reset the seek pointer

# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()