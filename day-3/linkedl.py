# The program implements a linked list data structure in Python. It defines classes for nodes (Node) and the linked list itself (LinkedList).
# The LinkedList class provides methods for printing the list (print_list) and appending elements (append). The example usage demonstrates creating 
# a linked list, appending elements to it, and printing its contents.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None

    def print_list(self):
        # Set current node to the head 
        cur_node = self.head
        # While current node is true print data 
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        # Create new node 
        new_node = Node(data)

        # Make new node as the head of the linked list 
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list
        # Set last node to head
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

llist = LinkedList()
llist.append("a")
llist.append("B")
llist.print_list()
