# using a hashtable to count individual items
# Linear, O(n)

# define a set of items we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "grape", "apple", "watermelon",
         "apple", "grape", "kiwi", "kiwi", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item and increment the count for each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

# printing the results
print(counter)