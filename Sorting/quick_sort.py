## A Quicksort Example

items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]

def quickSort(dataset, first, last):
    if first < last:
        #caculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivot_value = datavalues[first]
    # establish the upper and lower indexs
    lower = first + 1
    upper = last
    
    # start searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index
        while lower <= upper and datavalues[lower] <= pivot_value:
            lower += 1

        # TODO: advance the upper index
        while datavalues[upper] >= pivot_value and upper >= lower:
            upper -= 1
            
        # TODO: if the two indexs cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper

# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
