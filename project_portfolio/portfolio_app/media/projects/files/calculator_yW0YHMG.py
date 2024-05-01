def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Welcome to the calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter your choice (1/2/3/4): ")
    
    if operation in ('1', '2', '3', '4'):
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        
        if operation == '1':
            print(f"The result of {x} + {y} = {add(x, y)}")
        elif operation == '2':
            print(f"The result of {x} - {y} = {subtract(x, y)}")
        elif operation == '3':
            print(f"The result of {x} * {y} = {multiply(x, y)}")
        elif operation == '4':
            print(f"The result of {x} / {y} = {divide(x, y)}")
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    calculator()