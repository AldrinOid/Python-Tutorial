# add item in the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset.add("banana")  # adding duplicate item
print(thisset)

# add multiple items in the set
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)
thisset.update(["banana", "cherry"])  # adding duplicate items
print(thisset)

