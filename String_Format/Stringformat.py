# using string fprmat method
name = "John"
age = 30
greeting = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting)

# using positional arguments
greeting_positional = "Hello, my name is {0} and I am {1} years old. {0} is learning Python.".format(name, age)
print(greeting_positional)

# using keyword arguments
greeting_keyword = "Hello, my name is {name} and I am {age} years old.".format(name=name, age=age)
print(greeting_keyword)

# using format specifiers
pi = 3.14159
formatted_pi = "The value of pi is approximately {:.2f}".format(pi)
print(formatted_pi)

# using f-strings (Python 3.6+)
greeting_fstring = f"Hello, my name is {name} and I am {age} years old."
print(greeting_fstring)

formatted_pi_fstring = f"The value of pi is approximately {pi:.2f}"
print(formatted_pi_fstring)

# using dictionary for formatting
person = {'name': 'Alice', 'age': 25}
greeting_dict = "Hello, my name is {name} and I am {age} years old.".format(**person)
print(greeting_dict)

# using list for formatting
data = ['Bob', 22]
greeting_list = "Hello, my name is {} and I am {} years old.".format(*data)
print(greeting_list)

