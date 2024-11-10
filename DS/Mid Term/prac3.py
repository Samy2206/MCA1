# Apply the Circular SLL algorithm and Create Circular Singly linked 
# list and perform the following operations: insert from head, 
# insert from tail , insert from specified position and display
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circlList:
    def __init__(self):
        self.head=None

    def insert_beg(self,data):
        newNode = node(data)
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
        else:
            cNode=self.head
            while cNode.next != self.head:
                cNode=cNode.next
            newNode.next=self.head
            self.head=newNode
            cNode.next=self.head
    
    def insert_end(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
        else:
            cNode=self.head
            while cNode.next != self.head:
                cNode=cNode.next
            cNode.next=newNode
            newNode.next=self.head
        
    def insert_spec(self,data,loc):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
        elif loc==1:
            self.insert_beg(data)
        else:
            cNode=self.head
            cLoc=1
            while cNode.next!=self.head and cLoc<loc-1:
                cNode=cNode.next
                cLoc=cLoc+1
            newNode.next=cNode.next
            cNode.next=newNode

    def display(self):
        if self.head==None:
            print("Linked list is empty: ")
        else:
            cNode=self.head
            while cNode.next!=self.head:
                print(cNode.data,end="-->")
                cNode=cNode.next
            print(cNode.data)


cl = circlList()
cl.insert_beg(10)
cl.insert_beg(20)
cl.display()
cl.insert_end(40)
cl.insert_end(50)
cl.display()
cl.insert_spec(100,2)
cl.insert_spec(78,4)
cl.display()

