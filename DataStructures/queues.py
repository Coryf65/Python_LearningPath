# trying out a queue in Python
# you could ruse  alist but a deque is more effecient
from collections import deque

# creating a new empty deque object that will functin as a queue
queue = deque()

# add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the queue contents 
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)