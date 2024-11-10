# Create a class for Student and calculate () method implements grade for 5 Students. 
# Take appropriate inputs from user. (use list for 5 subject marks)
from functools import *
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def calculate(self):
        total=reduce(lambda x,y:x+y,self.marks)
        perc = total/5
        print(f"Percentage : {perc:.2f}")
        print("Grade: ",end="")
        if perc>75:
            print("A Grade")
        elif perc>60:
            print("B Grade")
        elif perc>50:
            print("C Grade")
        elif perc>35:
            print("D Grade")
        else:
            print("Failed")
        
    
    def display_name(self):
        print("Name : ",self.name)

students=[]
for i in range(1,6):
    name = input(f"Enter name of student {i}: ")
    marks =[int(x) for x in input("Enter marks of 5 subjects: ").split()]
    students.append(Student(name,marks))

for student in students:
    student.display_name()
    student.calculate()
    print("\n")


