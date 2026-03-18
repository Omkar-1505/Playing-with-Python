#it deals with the 0 index value of array
class stack:
    def __init__(self):
        self.s =[]
    
    def length(self):
        return len(self.s)
    
    def push(self,value):      #helps to avoid the checking of overflow
        self.s.insert(0,value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty") 
        else:
            return self.s[0]
        
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        else:
            return self.s.pop(0)
        
stk = stack()
stk.push(10)
stk.push(20)
print(stk.peek())
