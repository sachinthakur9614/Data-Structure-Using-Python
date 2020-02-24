

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data:
            if data <self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                
        else:
            self.data = data
    
    def find_val(self,key_val):
        if key_val<self.data:
            if self.left is None:
                return str(key_val) +"not found!"
            return self.left.find_val(key_val)
        elif key_val >self.data:
            if self.right is None:
                return str(key_val) +"not found!"
            return self.right.find_val(key_val)
        else:
            print(str(self.data)+'is found!')

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(10)
root.insert(13)
        
            
    

root.PrintTree()


