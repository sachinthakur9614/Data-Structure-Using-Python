class  Node(object):

    def __init__(self,data = None,next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next

        






class LinkedList(object):
    def __init__(self,head = None):
        self.head = head

    def __repr__(self):
        nodes = []

        current =  self.head
        while current:
            nodes.append(repr(current.get_data()))
            current = current.next_node
        return '[' + ','.join(nodes) + ']'
    

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    
    def size(self):
        current  = self.head
        count =0
        while current:
            count +=1
            current = current.get_next()

        return count

    def search(self,data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                return current.get_data()

            else:
                current = current.get_next()
            
            if current is None:
                raise ValueError("Data not in list")
        return current.get_data()
    
    def delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data()== data:
                found = True
            else:
                previous = current
                current = current.get_next
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            raise ValueError("Data not in list")

        else:
            previous.set_next(current.get_next)



    def reverse(self):
        current = self.head
        pre_node = None
        next_node = None
        while current:
            next_node = current.get_next()
            current.set_next = pre_node
            pre_node  = current
            current.set_next = next_node
        self.head = pre_node

f1  = LinkedList()

f1.insert(10)
f1.insert(20)
f1.insert(30)
f1.insert(40)
f1.insert(50)


print(f1)

