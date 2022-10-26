# Linked list Class

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

    def print_list(self):
        # head=>firstnode->2nd->3rd->4th->None
        currentNode = self.head
        while True:
            if currentNode is None:
                break
        print(currentNode.value)
        currentNode = currentNode.next

llist = LinkedList()
llist.append("First Node")
llist.append("2nd Node")
llist.append("3rd Node")
llist.append("4th Node")