class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circlList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            cNode = self.head
            while cNode.next != self.head:
                cNode = cNode.next
            newNode.next = self.head
            self.head = newNode
            cNode.next = self.head

    def delete_spec(self, loc):
        if self.head is None:
            print("Linked list is already empty")
            return
        if self.head.next == self.head and loc == 1:
            self.head = None
            print("After deletion, the list is empty")
            return
        if loc == 1:
            self.delete_beg()
            return
        cNode = self.head
        cLoc = 1
        while cNode.next != self.head and cLoc < loc - 1:
            cNode = cNode.next
            cLoc += 1
        if cNode.next == self.head:
            print("Position out of range")
            return
        cNode.next = cNode.next.next

    def delete_beg(self):
        if self.head is None:
            print("Linked list is already empty")
            return
        if self.head.next == self.head:
            self.head = None
            print("After deletion, the list is empty")
            return
        cNode = self.head
        while cNode.next != self.head:
            cNode = cNode.next
        self.head = self.head.next
        cNode.next = self.head

    def delete_end(self):
        if self.head is None:
            print("Linked list is already empty")
            return
        if self.head.next == self.head:
            self.head = None
            print("After deletion, the list is empty")
            return
        cNode = self.head
        while cNode.next.next != self.head:
            cNode = cNode.next
        cNode.next = self.head

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        cNode = self.head
        while cNode.next != self.head:
            print(cNode.data, end=" --> ")
            cNode = cNode.next
        print(cNode.data)

cl = circlList()
cl.insert_beg(10)
cl.insert_beg(20)
cl.insert_beg(30)
cl.insert_beg(40)
cl.insert_beg(50)
cl.display()
cl.delete_beg()
cl.display()
cl.delete_end()
cl.display()
cl.delete_spec(3)
cl.display()
