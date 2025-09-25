# using functions python
def greet(name): # this is a parameter
    """Function to greet a person with their name."""
    return f"Hello, {name}!"  
# Function call
print(greet("Alice")) # this is an argument

# using arbitrary arguments
def greet_all(*names):
    """Function to greet all persons in the names list."""
    for name in names:
        print(f"Hello, {name}!")
# Function call with arbitrary arguments
greet_all("Alice", "Bob", "Charlie")

# using keyword arguments
def describe_person(name, age):
    """Function to describe a person with their name and age."""
    return f"{name} is {age} years old."
# Function call with keyword arguments
print(describe_person(age=30, name="Alice"))

# using **kwargs
def describe_person_details(**details):
    """Function to describe a person with arbitrary details."""
    for key, value in details.items():
        print(f"{key}: {value}")
# Function call with arbitrary keyword arguments
describe_person_details(name="Alice", age=30, city="New York")

# using default parameters
def greet_with_default(name="Guest"):
    """Function to greet a person with a default name."""
    return f"Hello, {name}!"
# Function call without argument, uses default parameter
print(greet_with_default())

# using return statement
def add(a, b):
    """Function to add two numbers and return the result."""
    return a + b
# Function call and storing the return value
result = add(5, 3)
print(f"The sum is: {result}")

# using pass statement in functions
def placeholder_function():
    """This function does nothing for now."""
    pass  # Placeholder for future code
# Function call
placeholder_function()
print("This is a placeholder function.")

def access_items_list(my_list):
    for x in my_list:
        print(x)

my_list = [1, 2, 3, 4, 5]
access_items_list(my_list)

# using positional-only arguments
def pos_only_arg(arg, /):
    """Function with a positional-only argument."""
    return f"Positional-only argument: {arg}"
# Function call with positional argument
print(pos_only_arg("Hello"))

# using keyword-only arguments
def kw_only_arg(*, arg):
    """Function with a keyword-only argument."""
    return f"Keyword-only argument: {arg}"
# Function call with keyword argument
print(kw_only_arg(arg="Hello"))

# combining different types of arguments
def combined_args(pos_arg, /, kw_arg, *, default_arg="Default"):
    """Function combining different types of arguments."""
    return f"Positional: {pos_arg}, Keyword: {kw_arg}, Default: {default_arg}"
# Function call combining different types of arguments
print(combined_args("Pos", kw_arg="Key"))

# recursive function example
def factorial(n):
    """Function to calculate the factorial of a number recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Function call to calculate factorial
print(f"Factorial of 5 is: {factorial(5)}")

def tri_recursion(k):
  if k > 0:
    result = k + tri_recursion(k - 1)
  else:
    result = 0
  return result

print("Recursion Example Results:")
print(tri_recursion(6))

