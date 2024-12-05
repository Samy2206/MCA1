class parent:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name)

class child(parent):
    def __init__(self,age,name):
        super().__init__(name)
        self.age=age

    def display(self):
        print(self.age)
        super().display

c=child(21,'sam')
c.display()

