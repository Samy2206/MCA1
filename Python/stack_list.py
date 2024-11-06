class stack:
    def __init__(self):
        self.stack=[]
     
    def isEmpty(self):
        return len(self.stack)==0
    
    def stackPush(self,data):
        self.stack.append(data)
    
    def stackPop(self):
        if self.isEmpty():
            print("The stack is already empty")
        else:
            self.stack.pop()
    
    def display(self):
        if self.isEmpty():
            print("Empty Stack")
        else:
            print(self.stack)

s = stack()
s.stackPush(10)
s.stackPush(20)
s.stackPush(30)
s.display()
s.stackPop()
s.stackPop()
s.stackPop()
s.stackPop()
s.display()
    
