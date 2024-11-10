# Create a class Employee with function employe_details(), override
# parent class function in child class with addition of bonus=500 in 
# parent class function.
# Parent class Employee
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def employee_details(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
    
    def employee_details(self):
        bonus = 500
        total_salary = self.salary + bonus
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Bonus: {bonus}, Total Salary: {total_salary}"

employee = Employee("Sam", "Developer", 80000)
print("Employee Details (Parent Class):")
print(employee.employee_details())

manager = Manager("John", "Manager", 100000)
print("\nManager Details (Child Class with Bonus):")
print(manager.employee_details())
