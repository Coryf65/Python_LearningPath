# a Merge Sort Algoritm example

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_array = dataset[:mid]
        right_array = dataset[mid:]

        #TODO: recursively break down the arrays
        mergesort(left_array)
        mergesort(right_array)

        #TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                dataset[k] = left_array[i]
                i += 1
            else:
                dataset[k] = right_array[j]
                j += 1
            k += 1

        # TODO: if the left array still has values, add them
        while i < len(left_array):
            dataset[k] = left_array[i]
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(right_array):
            dataset[k] = right_array[j]
            j += 1
            k += 1

# testing the merge sorting with data
print(items)
mergesort(items)
print(items)