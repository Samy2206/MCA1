class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def display_role_manager(self):
        print("Role : Manager")

class Engineer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
       
    def display_role_engineer(self):
        print("Role : Engineer")

class ManagerEngineer(Manager, Engineer):
    def __init__(self, name, salary):
        Manager.__init__(self, name, salary) 
        Engineer.__init__(self, name, salary) 
        

obj = ManagerEngineer("John", 70000)
obj.display_info()
obj.display_role_engineer()  
obj.display_role_manager() 
