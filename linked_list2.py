# How to Traverse through linked list using a while loop

class Node:
    def __init__(self, value): #the attributes inside is what the user will be inputing, but you can still add attributes by defining them below
        self.value = value
        self.next = None

def iter_linked_list(node):
    while node is not None: # better to use "is not"/"is" when equality for None values
        print(node.value)
        node = node.next

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
head.next.next.next = Node("4th Node")

iter_linked_list(head)

# print(head.value)
# print(head.next.value)
# print(head.next.next.value

