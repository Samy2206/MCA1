# Create application to perform exception Handling , read data from text File
# and throw multiple exception in try and handle it with creating multiple 
# except block.


file_name = "data.txt"

try:
    with open(file_name, "w") as file:
        file.write("Hello, this is a test file.\n")
        file.write("Python exception handling demo.\n")
        file.write("Let's see how multiple exceptions are handled.\n")
except Exception as e:
    print(f"Error while creating the file: {e}")

def read_data_from_file():
    try:
        with open(file_name, "r") as file:
            data = file.readlines()

        print("File contents:")
        for line in data:
            print(line.strip())

        raise ValueError("A value error occurred!")
        raise IndexError("An index error occurred!")

    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {file_name}.")
    except IOError as e:
        print(f"Error: An I/O error occurred while reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("File read successfully without errors.")
    finally:
        print("Execution finished.")


# Calling the function to test exception handling
read_data_from_file()
