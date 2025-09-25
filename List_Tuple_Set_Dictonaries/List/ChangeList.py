list1 = ["apple", "banana", "cherry", "date", "elderberry"]

# changing the value of the first element
list1[0] = "apricot"
print("Updated List:", list1) 

# changing the value of a slice from index 1 to 3
list1[1:4] = ["blueberry", "cantaloupe", "dragonfruit"]
print("Updated List after slice change:", list1)

# changing the value of the last element
list1[-1] = "fig"
print("Updated List after changing last element:", list1)

# changing the value of a slice from the second last to the last element
list1[-2:] = ["grape", "honeydew"]
print("Updated List after changing last two elements:", list1)

# changing the value of every second element
list1[::2] = ["kiwi", "lemon", "mango"]
print("Updated List after changing every second element:", list1)

# changing the value of the entire list
list1[:] = ["nectarine", "orange", "papaya", "quince", "raspberry"]
print("Updated List after changing the entire list:", list1)

# changing the value of the entire list using another method
list1 = ["strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon"]
print("Updated List after reassigning the entire list:", list1)
print("Number 19.", list1[:]) # Accessing the entire list using another method
print("Number 20.", list1[::]) # Accessing the entire list