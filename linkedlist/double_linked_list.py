

class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head ==None:
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None

    
    def display(self):
        current  = self.head
        if self.head ==None:
            print("list is empty")
            return
        while(current!= None):
                
                print(current.data)
                current = current.next

    def append(self,data):
        new_node  = Node(data)
        new_node.next = None
        if self.head is None:
            new_node.previous = None
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.previous = current
        return





d = DoublyLinkedList()
d.addNode(1)
d.addNode(2)
d.addNode(3)
d.addNode(4)
d.addNode(5)

d.display()
