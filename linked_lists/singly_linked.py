# create node class
# create linked list class
# add nodes to linked list
# print linked list

class Node():
    def __init__(self, data):
        self.data = data 
        self.next = Node

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        # we have a linkedlist that points to John (head =>John->None)
        if self.head is None:
            self.head = newNode
        else:
            # head=>John->Ben->None || John -> Mateo
            lastNode = self.head
            while True:
                if lastNode.next is None: #if ur lastNode = None then it's your last Node in the list 
                    break
                lastNode = lastNode.next
            lastNode.ext = newNode
        
    def print_list(self):
        # head=>John->Ben->Mateo->None
        currentNode = self.head
        while True:
            if currentNode is None:
                break
        print(currentNode.data)
        currentNode = currentNode.next

# every Node will have data and next fields
firstNode = Node("John")
# calling class Node will instantiate an object
# firstNode.data = John, firstNode.next = None 
    # because firstNode.next is none value, it becomes the head node 
linkedList = LinkedList()
linkedList.insert(firstNode) #(head =>John=>None)
secondNode = Node("Benito")
linkedList.insert(secondNode)
thirdNode = Node("Mateo")
linkedList.insert(thirdNode)