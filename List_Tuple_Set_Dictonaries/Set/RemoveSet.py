# remove an item in the set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")  # raises an error if the item to remove does not exist
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")  # does not raise an error if the item to remove does not exist
print(thisset)  

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # removes a random item
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()  # removes all items
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset  # deletes the set completely
#print(thisset)  # this will raise an error because the set no longer exists
