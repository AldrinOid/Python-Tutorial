# list comprehension
list1 = [1,2,3,4,5,6,7,8,9,10]

# using list comprehension to create a new list with items that have more than 5
new_list = [item for item in list1 if item > 5]
print(new_list) # it will print the new list with items that have more than 5   

# using list comprehension to create a new list with items that are even
new_list = [item for item in list1 if item % 2 == 0]    
print(new_list) # it will print the new list with items that are even

# using list comprehension to create a new list with items that are odd
new_list = [item for item in list1 if item % 2 != 0]    
print(new_list) # it will print the new list with items that are odd

