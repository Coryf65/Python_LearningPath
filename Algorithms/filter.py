# use a hashtable to filter out duplicate items
# Linear, O(n)

# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "grape", "apple", "watermelon"]

# TODO: create a hashtable to perform a filter
filter = dict()

# TODO: loop over each item and add it into our hashtable
for key in items:
    filter[key] = 0

# TODO: create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)