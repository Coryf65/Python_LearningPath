## Linked List example 

# the nodes class
# a single linkedlist that has one field as val
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
    
# the LinkedList class 
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        #TODO: insert data
        # note: only going to insert items at the head
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        #TODO: find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def deleteAt(self, index):
        #TODO: delete an item at a given index
        if index > self.count - 1:
            return
        if index == 0:
            self.head = self.head.get_next()
        else:
            temp_index = 0
            node = self.head
            while temp_index < index - 1:
                node = node.get_next()
                temp_index += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    # prints our list data
    def dump_list(self):
        temp_node = self.head
        while (temp_node != None):
            print("Node: ", temp_node.get_data())
            temp_node = temp_node.get_next()

# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# exercise the list
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(13))
# print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()