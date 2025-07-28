# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input! Please enter numbers.")
finally:
    print("Execution completed.")
