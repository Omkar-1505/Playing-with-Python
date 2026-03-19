# working
# at beg; front = rear =-1
# 1st element insert ; front = 0 and rear =0
# insertion; rear = rear+1(Overflow)
# delete front = front+1 (underflow)

#python provides the power of append and pop 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.item) == 0
    
    def insert(self,value):
        self.items.append(value)

    def delete(self):
        if (self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
q = Queue()
q.insert(10)
q.insert(20)
print(q) #provides Address of object
print(q.delete())