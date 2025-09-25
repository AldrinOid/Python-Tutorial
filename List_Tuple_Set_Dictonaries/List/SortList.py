# sorting a list
list1 = [5,2,9,1,5,6]
list2 = ["banana", "apple", "cherry", "date"]

# using sort function
list1.sort() # it will sort the list in ascending order
print(list1)

list2.sort() # it will sort the list in alphabetical order
print(list2)

# using reverse parameter in sort function
list1.sort(reverse=True) # it will sort the list in descending order
print(list1)

# sort function is case sensitive
list3 = ["banana", "Apple", "Cherry", "date"]
list3.sort() # it will sort the list in alphabetical order but uppercase letters come before lowercase
print(list3)
list3.sort(key=str.lower) # it will sort the list in alphabetical order ignoring case
print(list3)

# using reversed function
list4 = [5,2,9,1,5,6]   
rev_list = reversed(list4) # it will return a reversed iterator object
print(list(rev_list)) # convert the iterator object to a list to see the reversed list