# Linked list Prepend Method

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        # New node comes with attribute as None, no memory address 

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return
# appended new node onto list when the list is empty 
# if head node has value then it skips code block to below
        node = self.head
        while node.next is not None:
            node = node.next   
        node.next = new_node
        print("Appended new Node with value:", node.next.value)
        # this is how to implement append method to linked list class

    def prepend(self, value):
        new_node = Node(value)
       
        if self.head is not None:
            self.head = new_node
            print("Head Node created: ",value)
            return
        else:
            new_node = self.head
            self.head = Node(value)
            self.head.next = oldhead
            print("Node following Head is: ",value)
        return

llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")