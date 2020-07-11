# determine if a list is sorted

items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 49, 56, 23, 87, 41, 49, 53]

def is_sorted(item_list):
    # TODO: using the brute force method, how you could to the pyhton comp in another language
    # for i in range(0, len(item_list) - 1):
    #     if (item_list[i] > item_list[i+1]):
    #         return False
    
    # using a python comprehension, if all are true it returns true if any are false it returns false
    return all(item_list[i] <= item_list[i+1] for i in range(len(item_list)-1))

    #return True

print(is_sorted(items1))
print(is_sorted(items2))