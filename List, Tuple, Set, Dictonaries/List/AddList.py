# add items in the list
list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = ["a", "b", "c", "d", "e"]

# using append function
list1.append(11)
print(list1) # the item will be added at the end of the list

# using insert function
list1.insert(13, 12)
print(list1) # specify the index where you want to add the item

# using extend function
list1.extend(list2)
print(list1) # the added list will be added at the end of the list

# you can use extend function for list with any iterable object like tuple, set, and dictionaries
