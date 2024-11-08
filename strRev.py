class stack:
    def __init__(self):
        self.stack=[]
        self.Top=-1
    
    def Push(self,data):
        self.stack.append(data)
        self.Top=len(self.stack)-1

    def Pop(self):
        if self.Top<0:
            print("Stack is Empty")
        else:
            return self.stack.pop()
        
    def display(self):
        if(self.Top<1):
            print("Stack is Empty") 
        else:
            print(self.stack)

s=stack()
data=input("Enter the string to revserse: ")
res=""
for i in data:
    s.Push(i)

for i in range(len(data)):
    res=res+s.Pop()

print(res)
