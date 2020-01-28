class Node(object):
    def  __init__(self,key,next = None):
        self.key = key
        self.next = None
    
    def __str__(self):
        return str(self.key)
    
    def __repr__(self):
        return str(self.key)



class CircularLinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def append(self,key):
        new_node = Node(key)

        if self.head is None:
            self.head =  new_node
            new_node.next = self.head
        else:
            current_node = self.head
             while current_node.next!= self.head:
                 current_node = current_node.next
            current_node.next= new_node
            new_node.next= self.head
    
    def prepend(self,key):
        new_node = Node(key)

        current_node = self.head
        new_node.next = self.head

        if self.head is None:
            new_node.next = new_node
        else:
            while current_node.next!= self.head:
                current_node = current_node.next
            
            current_node.next = new_node
        self.head = new_node


    def insert_after_key_node(self,next_key,key):
        currrent_node = self.head
        while current_node:
            if currrent_node.next == self.head and currrent_node.key == next_key:
                self.append(key)
                return
            
            elif currrent_node.key == next_key:
                new_node = Node(key)
                new_node = currrent_node.next
                currrent_node.next = new_node
                new_node.next = new_node

            else:
                if currrent_node.next == self.head:
                    break
            currrent_node = currrent_node.next

        
        def delete(self,delete_key):
            currrent_node = self.head
            pre_node = None
            while current_node:
                
                if currrent_node.key == delete_key and currrent_node == self.head:
                    if currrent_node.new_node == self.head:
                        currrent_node = None
                        self.head = None

                    else:
                        while currrent_node.next!= self.head:
                            currrent_node = currrent_node.next
                        
                        currrent_node.next = self.head.next
                        self.head = self.head.next
                        currrent_node = None
                        return
                elif currrent_node.key == delete_key:
                    pre_node.next = currrent_node.next
                    currrent_node = None
                    return
                else: 
                    if currrent_node.next ==self.head:
                        break
                pre_node = currrent_node
                currrent_node = currrent_node.next