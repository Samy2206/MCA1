# Q.01 Demonstrate multiple inheritance with a "Smartphone" subclass.
# Solution →
class Phone:
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

    def make_call(self):
        print(self.brand, "calling to", self.number)

    def send_message(self, message):
        print("Message to", self.number, ":", message)


class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print("Taking a photo with", self.resolution, "resolution.")

    def record_video(self):
        print("Recording video with", self.resolution, "resolution.")


class Smartphone(Phone, Camera):
    def __init__(self, brand, number, resolution):
        Phone.__init__(self, brand, number)
        Camera.__init__(self, resolution)


# Instantiate the Smartphone class and test the functionality.
smartphone = Smartphone("Samsung", "702879078", "108MP")
smartphone.make_call()
smartphone.send_message("Hello!")
smartphone.take_photo()
smartphone.record_video()

# Output →
# Samsung calling to 702879078
# Message to 702879078 : Hello!
# Taking a photo with 108MP resolution.
# Recording video with 108MP resolution.

# ----------------------------------------------------

# Q.02 Multithreading: One thread prints the square, another prints the cube of a number.
# Solution →
from threading import Thread
import time

def square(n):
    print("Square:", n * n)

def cube(n):
    print("Cube:", n * n * n)


# Input value
n = 5

# Measure execution time
start_time = time.time()

# Create threads
t1 = Thread(target=square, args=(n,))
t2 = Thread(target=cube, args=(n,))

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

end_time = time.time()

print("Total time of execution =", end_time - start_time)

# Output →
# Square: 25
# Cube: 125
# Total time of execution = [Execution time may vary]

# ----------------------------------------------------

# Q.03 Synchronization of threads using RLock to calculate factorials.
# Solution →
import threading

def factorial(number, lock):
    with lock:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        print(f"Factorial of {number}: {fact}")


def main():
    lock = threading.RLock()

    try:
        # Input two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Create threads
        thread1 = threading.Thread(target=factorial, args=(num1, lock))
        thread2 = threading.Thread(target=factorial, args=(num2, lock))

        # Start threads
        thread1.start()
        thread2.start()

        # Wait for threads to complete
        thread1.join()
        thread2.join()

    except ValueError:
        print("Please enter valid integers!")


main()

# Output →
# Enter the first number: 5
# Enter the second number: 4
# Factorial of 5: 120
# Factorial of 4: 24

# ----------------------------------------------------

# Q.04 Validate Email ID using a regular expression.
# Solution →
import re

def validate(email):
    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        print(email, "is a valid email ID.")
    else:
        print(email, "is not a valid email ID.")


# Input email for validation
email = input("Enter an email ID to validate: ")
validate(email)

# Output →
# Enter an email ID to validate: hello123@gmail.com
# hello123@gmail.com is a valid email ID.

# ----------------------------------------------------

# Q.05 MongoDB operations for "employee" collection.
# Solution →
from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["company1"]
emp = db["employee"]

# Sample data
sample_data = [
    {"ID": 1001, "name": "Sanjana", "address": "Mumbai", "phone": "5551234567", "email": "sanjana@gmail.com", "dept": "HR"},
    {"ID": 210345, "name": "Sanket", "address": "Chinchvad", "phone": "5559876543", "email": "sam@gmail.com", "dept": "Accounts"},
    {"ID": 1003, "name": "Sandesh", "address": "Lonavala", "phone": "5551112222", "email": "sandesh@gmail.com", "dept": "Accounts"},
    {"ID": 1004, "name": "Sanketi", "address": "Pune", "phone": "5553334444", "email": "sanketi@gmail.com", "dept": "IT"},
    {"ID": 123, "name": "Tanmay", "address": "Pune", "phone": "5553334444", "email": "tanmay@gmail.com", "dept": "IT"},
]

# Insert sample data into collection
emp.insert_many(sample_data)

# i) Display employees in "Accounts" department
print("Employees in 'Accounts' department:")
accounts_employees = emp.find({"dept": "Accounts"})
for e in accounts_employees:
    print(e)

# ii) Delete employee with ID - 210345
delete_result = emp.delete_one({"ID": 210345})
if delete_result.deleted_count > 0:
    print("\nEmployee with ID - 210345 has been deleted.")
else:
    print("\nNo employee found with ID - 210345.")

# iii) Update phone for employee ID - 123
new_phone = "5559998888"
update_result = emp.update_one({"ID": 123}, {"$set": {"phone": new_phone}})
if update_result.modified_count > 0:
    print(f"\nEmployee with ID - 123's phone number has been updated to {new_phone}.")
else:
    print("\nNo employee found with ID - 123 to update.")

# Display updated collection
print("\nUpdated employee collection:")
for e in emp.find():
    print(e)

client.close()

# Output →
# Employees in 'Accounts' department:
# [Employee data from "Accounts"]
# Employee with ID - 210345 has been deleted.
# Employee with ID - 123's phone number has been updated to 5559998888.
# [Updated employee collection]

# ----------------------------------------------------

# Q.06 Validate password using given criteria.
# Solution →
import re

def validate_password(password):
    # Define the regex pattern for a valid password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@#*])[A-Za-z\d$@#*]{8,20}$'

    # Check if the password matches the pattern
    if re.match(pattern, password):
        print(password, "is a valid password.")
    else:
        print(password, "is not a valid password.")


# Input password for validation
password = input("Enter a password to validate: ")
validate_password(password)

# Output →
# Enter a password to validate: MySecure@123
# MySecure@123 is a valid password.
