def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(f"{num1} + {nume2} = {add(num1, num2)}")

elif operation == "-":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif operation == "*":
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif operation == "/":
    print(f"{num1} / {num2} = {divide(num1, num2)}")

else:
    print("Invalid operation!")

