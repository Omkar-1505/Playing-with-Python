#edge cases check #go for top down relation too 
class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self): #head is never moved else stays at 1st location only
        self.head = None
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if (self.head==None):
            self.head = temp
            return
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev=t

    def printDLL(self):
        t = self.head
        # Traverse through the list and print each node
        while t is not None:
            print(t.data, end="<-->")
            t = t.next
        print()  # newline at end

    def insertAtBeg(self,value):
        temp = Node(value)
        if (self.head==None):
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insertAtMid(self,value,val):
        t=self.head
        while(t.next != None):
            if (t.data == val): #searching
                break
            else:
                t = t.next
        temp = Node(value) 
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def DeleteDLL(self,value):
        t = self.head
        if (t.data == value):   #Deleting first
            self.head = t.next
            self.head.prev = None
            return 
        while(t.next != None):    #Delete at middle
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if (t.data == value):
            t.prev = None


obj = DoubleLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtBeg(5)
obj.insertAtMid(15,10)
obj.printDLL()
obj.DeleteDLL(5)
obj.printDLL()
obj.DeleteDLL(15)
obj.printDLL()