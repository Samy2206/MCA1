# Apply Stack Algorithm and create Stack using array and perform 
# following operations: Push, POP, Peek

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            return("Underflow - Stack is empty")
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return("Underflow - Stack is empty")
        else:
            return self.stack[-1]
    
    def display(self):
        if self.isEmpty():
            return("Underflow - Stack is empty")
        else:
            print(self.stack)

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Stack Top : ",s.peek())
print("Popped :",s.pop())
print("Popped :",s.pop())
s.display()
