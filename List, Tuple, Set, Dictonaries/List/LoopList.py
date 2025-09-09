# looping in the list
list1 = ["apple", "banana", "cherry", "date", "elderberry", "kiwi"]

# using for loop
for item in list1:
    print(item) # it will print each item in the list   

# using while loop
i = 0
while i < len(list1):
    print(list1[i]) # it will print each item in the list
    i += 1

# using list comprehension
[print(item) for item in list1] # it will print each item in the list

# using enumerate function
for index, item in enumerate(list1):
    print(f"Index: {index}, Item: {item}") # it will print the index and item in the list

# using map function
list(map(lambda item: print(item), list1)) # it will print each item in the list
list1 = [item for item in list1 if item != "cherry"] # it will remove "cherry" from the list
print(list1) # it will print the updated list without "cherry"

# using list comprehension to create a new list with items that have more than 5 characters
new_list = [item for item in list1 if len(item) > 5]    
print(new_list) # it will print the new list with items that have more than 5 characters

# using filter function to create a new list with items that have more than 5 characters
new_list = list(filter(lambda item: len(item) > 5, list1))
print(new_list) # it will print the new list with items that have more than 5 characters

# using zip function to loop through two lists
list2 = ["fig", "grape", "honeydew"]
for item1, item2 in zip(list1, list2):
    print(f"Item from list1: {item1}, Item from list2: {item2}") # it will print items from both lists

# If the lists have different lengths, zip will stop at the shortest one.