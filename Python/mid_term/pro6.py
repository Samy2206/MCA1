# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, 
# and emp_department and methods like calculate_emp_salary, 
# emp_assign_department, and print_employee_details.
#  Use 'print_employee_details' method to print the details of an employee.
#  Use 'assign_department' method to change the department of an employee.
#  Use 'calculate_emp_salary' method which takes two arguments: salary and 
# hours_worked, which is the number of hours worked by the employee. If the 
# number of hours worked is more than 50, the method computes overtime 
# and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))
class Employee:
    def __init__(self):
        self.emp_id = input("Enter Employee ID: ")
        self.emp_name = input("Enter Employee Name: ")
        self.emp_salary = float(input("Enter Employee Salary: "))
        self.emp_department = input("Enter Employee Department: ")
        self.hours_worked=int(input("Enter the hours worked by the employee: "))

    def calculate_emp_salary(self):
        hours_worked=self.hours_worked
        salary=self.emp_salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (salary / 50)
            total_salary = salary + overtime_amount
        else:
            total_salary = salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

emp=Employee()
emp.emp_assign_department("Sales")
emp.print_employee_details()
print("Salary after overtime: ",emp.calculate_emp_salary())
