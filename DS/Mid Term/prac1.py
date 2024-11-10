# Apply the DDL algorithm and Create doubly linked list and 
# perform the following operations: insert from head, insert from 
# tail , insert from specified position and display

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_head(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    
    def insert_tail(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
    
    def insert_spec(self,data,loc):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        elif loc==1:
            self.insert_head(data)
        else:
            cNode=self.head
            cLoc=1
            while cNode is not None and cLoc<loc-1:
                cNode=cNode.next
                cLoc+=1
            newNode.next=cNode.next
            cNode.next.prev=newNode
            newNode.prev=cNode
            cNode.next=newNode

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

dll=DLL()
dll.insert_head(10)
dll.insert_head(20)
dll.display()
dll.insert_tail(40)
dll.insert_tail(50)
dll.display()
dll.insert_spec(100,2)
dll.insert_spec(75,5)
dll.display()
