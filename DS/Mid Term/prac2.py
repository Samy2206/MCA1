# Apply the DDL algorithm and Create doubly linked list and 
# perform the following operations: delete from head, delete from 
# tail , delete from specified position and display

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

    def del_head(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            self.head=self.head.next
            self.head.prev=None

    
    def del_tail(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            self.tail=self.tail.prev
            self.tail.next.prev=None
            self.tail.next=None
    
    def del_spec(self,loc):
        if self.head is None:
            print("Linked list is Empty")
        elif loc==1:
            self.del_head()
        else:
            cNode=self.head
            cLoc=1
            while cNode is not None and cLoc<loc-1:
                cNode=cNode.next
                cLoc+=1
            if cNode.next.next:
                cNode.next=cNode.next.next
                cNode.next.prev=cNode
            else:
                cNode.next=None

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

dll=DLL()
dll.insert_head(10)
dll.insert_head(20)
dll.insert_head(30)
dll.insert_head(40)
dll.insert_head(50)
dll.display()
dll.del_head()
dll.display()
dll.del_tail()
dll.display()
dll.del_spec(3)
dll.display()
