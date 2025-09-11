# using for loop to iterate over a list
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# using break statement to exit a loop
for item in my_list:
    if item == 3:
        break
    print(item)

# using continue statement to skip an iteration
for item in my_list:
    if item == 3:
        continue
    print(item)

# using range function to generate a sequence of numbers
for i in range(5):
    print(i)

# using range function with start and end values
for i in range(2, 5):
    print(i)

# using range function with step value
for i in range(0, 10, 2):
    print(i)

# using else clause with for loop
for item in my_list:
    print(item)
else:   
    print("Loop is finished")

# nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# using for loop to iterate over a string
my_string = "Hello"
for char in my_string:
    print(char)

# using for loop to iterate over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

# using pass statement in a loop
for item in my_list:
    if item == 3:
        pass  # Placeholder for future code
    print(item)
