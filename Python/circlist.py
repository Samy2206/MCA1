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

    def delete_spec(self,loc):
        if self.head==None:
            print("Linked list is already empty")
            return
        if self.head.next==self.head:
            self.head==None
            print("After deletion list is empty")
        else:
            cNode=self.head
            cLoc=1
            while cNode.next!=self.head and cLoc<loc-1:
                cNode=cNode.next
                cLoc=cLoc+1
            cNode.next=cNode.next.next


    def delete_beg(self):
        if self.head==None:
            print("Linked list is already empty")
            return
        if self.head.next==self.head:
            self.head==None
            print("After deletion list is empty")
        else:
            cNode=self.head
            while cNode.next!=self.head:
                cNode=cNode.next
            self.head=self.head.next
            cNode.next=self.head
        
    def delete_end(self):
        if self.head==None:
            print("Linked list is already empty")
            return
        if self.head.next==self.head:
            self.head==None
            print("After deletion list is empty")
        else:
            cNode=self.head
            while cNode.next.next!=self.head:
                cNode=cNode.next
            cNode.next=self.head
        

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
cl.insert_beg(30)
cl.insert_end(40)
cl.insert_end(50)
cl.insert_end(100)
cl.display()
cl.delete_beg()
cl.display()
cl.delete_end()
cl.display()
cl.insert_spec(200,3)
cl.display()
cl.delete_spec(4)
cl.display()

        
