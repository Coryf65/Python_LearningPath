# using a hashtable

# creating a hashtable all at once
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})

# seeing our hashtable
print(items1)

# creating a hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# trying to access a nonexistent key
#print(items1["key6"])

# replace an item
items2["key2"] = "two"

print(items2)

# iterating the keys and the values in the dictionary
for key, value in items2.items():
    print("Key: ", key, " Value:", value)