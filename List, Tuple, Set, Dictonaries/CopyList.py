# copy a list
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ["a", "b", "c", "d", "e"]

# using copy function
list3 = list1.copy()
print("list1:", list1)
print("list3 (copy of list1):", list3)

# using list function
list4 = list(list2)
print("list2:", list2)
print("list4 (copy of list2):", list4)

# using slicing
list5 = list1[:]
print("list5 (copy of list1 using slicing):", list5)
