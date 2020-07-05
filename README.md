# Python_LearningPath

Learning Python for fun !

## Algorithm Overview

- Complexity 

    - Space complexity: How much memeory does it require?

    - Time Complexity: How much time does it take to complete?

- Inputs and Outputs

    - What does the algorithm accept, and what are the results?

- Classification

    - Serial / Parallel, exact / approximate,
        deterministic / non-deterministic

-Common Algorithms

    - Searching

    - Sorting

    - Computational (take data and derive another)

    - Collection (filtering out data, counting)

- Performance

    - Big-O notation

*a good amount, not an exhaustive list*
| Notation  | Description | Example |
| --------- | ----------- | ------- |
| 0(1)  | Constant time  |  Looking up a single element in an array  |
| 0(log n)  | Logarithmic  |  Finding an item in a sorted array with a binary search  |
| 0(n)  | Linear time  |  Searching an unsorted array for a specific value  |
| 0(n log n)  | Log-linear |  Complex sorting algorithms like heap sort and merge sort  |
| 0(n^2)  | Quadratic  |  Simple sorting alorithms, such as bubble sort, selection sort, and insertion sort  |


## Data Structures

Used to organize data so it can be processed

    - Common Data Structures

        - Arrays
        - Linked lists 
        - Stacks and queues
        - Trees
        - Hash tables

1. Arrays :

[code example](/DataStructures/arrays.py)

a collection of elements identified by an index or key

Can be Multi-Demensional Arrays

- Array Operations

    - Calculate item index: O(1)
    - Insert or delete item at beginning: O(n)
    - Insert or delete item at middle: O(n)
    - Insert or delete item at end: O(1)

2. Linked lists

[code example](/DataStructures/Linkedlist.py)

    - Collection of data elements, called nodes
    - Contain reference to the next node in the list
    - Hold whatever data the application needs

3. Stacks and Queues

    - stack: 
    a collection that supports push and pop operations
    the last item pushed is the first one popped

    When to use

        - Expression processing
        - Backtracking: browser back button, for example

    - queue
    collection that supports adding and removing
    FIFO (first item in is the first one out)

    When to use

        - Order processing

        - Messaging

4. Hash Tables (sometimes called Dictionaries in other languages)

[code example](/DataStructures/hashtable.py)
an associative array

- key to value mappings and are unique
- hash tables are typically fast
- for small datasets, arrays are usually more effecient
- Hash tables don't order entries in a predictable way

## Recursion

when a function calls itself

these need to have a breaking condition. This prevents am infinite loop and eventual crashes
Each time the function is called, the old arguments are saved
this is called the "Call Stack"

exampes

1. [a Countdown](/Recursion/countdown.py)
2. [a Math based, Power and Factorial](/Recursion/recursion.py)

## Sorting Data

most modern languages have sorting built in

- the bubble sort - good for learning
- the merge sort
- the quick sort

### The Bubble Sort

- very simple to understand and implement
- Performance: O(n^2)
    for loops inside of for loops are usually n^2
- Other sorting algorithms are generally much better
- Not considered to be a practical solution
- Generally used for understanding the concepts

```python
# an example Bubble Sorting Algorithm

def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)

def main():
    list1 = [6, 20, 10, 19, 56, 21, 87, 41, 8, 53, 2]
    bubbleSort(list1)
    print("Result: ", list1)

if __name__ == "__main__":
    main()
```

### Merge Sort

[a Merge Sort Example](/Sorting/merge_sort.py)

parts data in half and half then sorts either side then merge

- a Divide and Concuer algorithm
- breaks a dataset into individual pieces and merges them
- Uses recursion to operate on datasets
- Performs well on large sets of data
- Log-Linear, Performance of O(n log n) time complexity

### The Quicksort

[a Quick Sort Example](/Sorting/quick_sort.py)

Pivot point selection

- Divide and conquer alogrithm, like the merge sort
- Also uses recursion to perform sorting
- Generally performs better than the merge sort, O(n log n)
- Operates in place on the data
- Worst case is O(n2) when data is mostly sorted already

## Searching

### Unsorted Searching

[Unsorted Search Example](/Sorting/unordered_searching.py)

### Sorted Searching

[Sorted Search Example](/Sorting/sorted_searching.py)

can use a binary search
this is faster than a unsorted search
log arithmic time scale

### Checking if a list is Sorted

[Is_Sorted Example](/Sorting/Is_sorted_checking.py)

linear time complexity