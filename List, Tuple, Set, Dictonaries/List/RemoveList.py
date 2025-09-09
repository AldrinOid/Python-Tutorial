# remove item in the list
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2 = ["a", "b", "c", "d", "e"]

# using remove function
list1.remove(5)
print(list1) # specify the item you want to remove

# using pop function
list1.pop() # if you don't specify the index, it will remove the last item
print(list1)
list1.pop(0) # specify the index of the item you want to remove
print(list1)

# using del function
del list1[0] # specify the index of the item you want to remove
print(list1)
del list2[1:3] # specify the slice of items you want to remove
print(list2)

# using clear function
list2.clear() # it will remove all the items in the list
print(list2)
print("Length of list2 after clear:", len(list2)) # it will return 0 as the length of the list
list2 = ["a", "b", "c", "d", "e"]
print("Length of list2 after reassigning:", len(list2)) # it will return 5 as the length of the list after reassigning

# using del function to delete the entire list
del list2
#print(list2) # it will raise an error as the list is deleted

# using slicing to remove items
list1 = [1,2,3,4,5,6,7,8,9,10]
list1[2:5] = [] # it will remove items from index 2 to 4
print(list1)

list1[::2] = [] # it will remove every second item
print(list1)    

list1[:] = [] # it will remove all the items in the list
print(list1)
print("Length of list1 after removing all items using slicing:", len(list1)) # it will return 0 as the length of the list
list1 = [1,2,3,4,5,6,7,8,9,10]
print("Length of list1 after reassigning:", len(list1)) # it will return 10 as the length of the list after reassigning

# using filter function to remove items
list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = list(filter(lambda x: x%2 == 0, list1)) # it will remove all the odd numbers from the list
print(list1) # it will return only even numbers in the list

# using list comprehension to remove items
list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = [x for x in list1 if x%2 == 0] # it will remove all the odd numbers from the list
print(list1) # it will return only even numbers in the list

