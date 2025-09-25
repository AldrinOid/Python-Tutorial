list1 = ["apple", "banana", "cherry", "date", "elderberry"]
print("Number 1.", list1[0])  # Accessing the first element

print("Number 2.", list1[2])  # Accessing the third element

print("Number 3.", list1[-1]) # Accessing the last element

print("Number 4.", list1[-3]) # Accessing the third last element

print("Number 5.", list1[1:4]) # Accessing a slice from index 1 to 3

print("Number 6.", list1[:3])  # Accessing the first three elements

print("Number 7.", list1[2:])  # Accessing elements from index 2 to the end

print("Number 8.", list1[-4:-1]) # Accessing a slice from the fourth last to the second last element

print("Number 9.", list1[::2]) # Accessing every second element

print("Number 10.", list1[::-1]) # Accessing the list in reverse order

print("Number 11.", list1[1:5:2]) # Accessing elements from index 1 to 4 with a step of 2

print("Number 12.", list1[-5:-1:2]) # Accessing elements from the fifth last to the second last with a step of 2

print("Number 13.", list1[::3]) # Accessing every third element

print("Number 14.", list1[::-2]) # Accessing every second element in reverse order

print("Number 15.", list1[1:4:-1]) # Accessing elements from index 1 to 3 in reverse order (will return an empty list)

print("Number 16.", list1[-1:-5:-1]) # Accessing elements from the last to the fifth last in reverse order

print("Number 17.", list1[::]) # Accessing the entire list

print("Number 18.", list1[:]) # Accessing the entire list using another method