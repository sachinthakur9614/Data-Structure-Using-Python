
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items ==[]
    
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    


q = Queue()

while True:
    print("Enqueue")
    print("Dequeue")
    print('quit')
    do = input("What you would like to do?").split()
    operation = do[0].strip().lower()

    if operation =='Enqueue':
        q.enqueue(int(do[1]))
    elif:
        if q.is_empty():
            print("Queue is empty")

        else:
            print("Dequeued value:",q.dequeue())
    elif operation =='quit':
        break
    