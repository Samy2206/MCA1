# Apply the Circular DLL algorithm and Create Circular 
# Doubly linked list and perform the following operations: delete 
# from head, insert from tail , delete from specified position and 
# display
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class circlList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        newNode = node(data)
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
        else:
            cNode = self.head
            while cNode.next != self.head:
                cNode = cNode.next
            newNode.next = self.head
            newNode.prev = cNode
            self.head.prev = newNode
            self.head = newNode
            cNode.next = self.head

    def delete_head(self):
        if self.head == None:
            print("Linked list is already empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            cNode = self.head
            while cNode.next != self.head:
                cNode = cNode.next
            self.head = self.head.next
            self.head.prev = cNode
            cNode.next = self.head

    def delete_tail(self):
        if self.head == None:
            print("Linked list is already empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            cNode = self.head
            while cNode.next != self.head:
                cNode = cNode.next
            cNode.prev.next = self.head
            self.head.prev = cNode.prev

    def delete_spec(self, loc):
        if self.head == None:
            print("Linked list is already empty")
        elif loc == 1:
            self.delete_head()
        else:
            cNode = self.head
            cLoc = 1
            while cNode.next != self.head and cLoc < loc:
                cNode = cNode.next
                cLoc += 1
            if cNode == self.head:
                print("Location exceeds the length of the list")
            else:
                cNode.prev.next = cNode.next
                cNode.next.prev = cNode.prev

    def display(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            cNode = self.head
            while cNode.next != self.head:
                print(cNode.data, end="<-->")
                cNode = cNode.next
            print(cNode.data)
        

cl = circlList()
cl.insert_beg(10)
cl.insert_beg(20)
cl.insert_beg(30)
cl.insert_beg(40)
cl.insert_beg(50)
cl.display()
cl.delete_head()
cl.display()
cl.delete_tail()
cl.display()
cl.delete_spec(2)
cl.display()

