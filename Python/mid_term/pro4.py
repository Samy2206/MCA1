# Create a perform exceptionHandling accept list from the user throw an exception in 
# try and handle it with creating multiple except block,else block and finally block.

def exception_handling():
    try:
        num=[int(x) for x in input("Enter the integers saperated by space: ").split()]
        total=sum(num)
        print("The total of integers is: ",total)
    except ValueError:
        print("Invalid input. Please enter integers only!")
    except KeyboardInterrupt:
        print("\nInput interepted by user!")
    else:
        print("Successfully enterd the list of integers!")
    finally:
        print("The execution of program is completed")

exception_handling()