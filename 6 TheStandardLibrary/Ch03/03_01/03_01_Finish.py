# Command Line Arguments
import sys

# Print Number of Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv)

# Remove Arguments, getting rid of the file pathing argument
print('Removing First Argument...')
sys.argv.remove(sys.argv[0])

print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg) # Casting into an number
        sum = sum + number
    except Exception:
        print("Bad input") # it is NaN so we throw an error

print(sum)