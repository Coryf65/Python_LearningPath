# Searching for an item in an unordered list
# sometimes called linear search
# Big O of linear time complexity

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_items(item, item_list):
    for i in range(0, len(items)):
        if item == item_list[i]:
            return i

    # item does not exist
    return None 

print(find_items(87, items))
print(find_items(250, items))