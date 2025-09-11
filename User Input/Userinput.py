# using user input to get a number and print its square
num = int(input("Enter a number: "))
print("The square of the number is:", num * num)

# using user input to get a string and print its length
text = input("Enter a string: ")
print("The length of the string is:", len(text))

# using user input to get a float and print its half
flt = float(input("Enter a float number: "))
print("Half of the float number is:", flt / 2)

# using user input to get a list of numbers and print their sum
numbers = input("Enter a list of numbers separated by spaces: ")
num_list = list(map(int, numbers.split()))
print("The sum of the numbers is:", sum(num_list))

# using user input to get a name and print a greeting message
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome!")

# using user input to get a date and print it in a different format
date = input("Enter a date (YYYY-MM-DD): ")
year, month, day = date.split('-')
print("The date in DD/MM/YYYY format is:", f"{day}/{month}/{year}") 

# using user input to get a sentence and print it in uppercase
sentence = input("Enter a sentence: ")  
print("The sentence in uppercase is:", sentence.upper())

# using user input to get a temperature in Celsius and convert it to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", fahrenheit)

# using user input to get a number and check if it's even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# using user input to get a list of words and print them sorted
words = input("Enter a list of words separated by spaces: ")
word_list = words.split()
word_list.sort()
print("The sorted list of words is:", word_list)

