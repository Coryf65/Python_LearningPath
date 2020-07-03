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