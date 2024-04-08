# Linked list
class Node:
    # constructor
    def __init__ (self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__ (self):
        self.head = None


    def print_list(self):
        cur_node = self.head
        while cur_node: 
            print(cur_node.data)
            cur_node = cur_node.next
    
    def append(self, data):
        new_node = Node(data)
        # check if list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # set beginning of list to last node 
        last_node = self.head
        # while the next pointer of the node currently on is not null
        while last_node.next:
            last_node = last_node.next

            # insert node
            
            
        last_node.next = new_node 


llist = LinkedList()
llist.append("A")
llist.append("B")      
llist.print_list()