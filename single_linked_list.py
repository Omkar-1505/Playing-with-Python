#here classes are also used 
class Node:
    def __init__(self,info,next=None):   #likes a constructor
        self.data=info
        self.next=next

class SinglyLinkedlist:
    def __init__ (self,head=None):
        self.head = head
    
    def insertAtEnd(self,value):   #we have to write everytime self explicitely to make it understand that the address of the calling linked list(not to be done in other OOPs language)
        temp = Node(value)  #constructor call
        if(self.head!= None):
            t1 = self.head
            while(t1.next!=None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printLL(self):
        if(self.head!= None):
            t1 = self.head
            while(t1.next!=None):
                print(t1.data)
                t1 = t1.next
            print(t1.data) #for last location

    def InsertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def InsertAtMiddle(self,value,val):   #val is the value after which you are inserting the value
        temp = Node(value)
        t1 = self.head
        while t1 != None:  # Check all nodes, including the last
            if t1.data == val:
                temp.next = t1.next
                t1.next = temp
                break  # Stop after inserting (assuming no duplicates; remove if you want to insert after all matches)
            t1 = t1.next
       
    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next

obj = SinglyLinkedlist()
obj.insertAtEnd(10)
obj.InsertAtBeg(6)
obj.InsertAtMiddle(40,10)
obj.insertAtEnd(20)
obj.printLL()
obj.deleteLL(40)
obj.printLL()
obj.deleteLL(20)
obj.printLL()





