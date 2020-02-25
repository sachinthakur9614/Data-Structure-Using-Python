

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
    
    def delete_node(self,root,key):
        if not root:
            return root
        if root.data >key:
            root.left = self.delete_node(root.left,key)
        elif root.data < key:
            root.right = self.delete_node(root.right,key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            temp_val  = root.right
            mini_val = temp_val.data
            while temp_val.left:
                temp_val = temp_val.left
                mini_val =  temp_val.data
            root.data = mini_val

            root.right = self.delete_node(root.right,root.data)
        return root

    
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
    
    def post_order(self,root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)
    
    def in_order(self,root):
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def pre_order(self,root):
        if root:
            print(root.data)
            self.pre_order(self.left)
            self.pre_order(self.right)



root = Node(12)
root.insert(6)
root.insert(10)
root.insert(13)
        
            
    

root.PrintTree()


