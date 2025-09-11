# using python try except to handle exceptions

# handling division by zero error
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# handling invalid input error
try:
    user_input = int(input("Enter an integer: "))
    print("You entered:", user_input)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# handling file not found error
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.") 

# handling multiple exceptions
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
finally:
    print("Execution completed.")

# handling index error
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: List index out of range.")    

# handling key error in dictionary
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError:
    print("Error: Key not found in dictionary.")

# using else block with try except
try:
    num = int(input("Enter a number: "))    
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print("You entered:", num)
finally:
    print("Execution completed.")