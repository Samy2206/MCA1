# Apply Stack Algorithm and create Stack using linked list and 
# perform following operations: Push, POP, Peek

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
    
class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        newNode=Node(data)
        if self.top is None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
    
    def pop(self):
        if self.top is None:
            return "Stack is empty"
        else:
            popped_node=self.top
            self.top=self.top.next
            popped_node.next=None
            return popped_node.data
        
    def peek(self):
        if self.top is None:
            return "Stack is empty"
        else:
            return self.top.data
    
    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            print("----")
            while temp:
                print(temp.data)
                print("----")
                temp=temp.next
            
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("After pushing: ")
s.display()
print("Popped Element :",s.pop())
print("After popping: ")
s.display()
print("Stack Top :",s.peek())