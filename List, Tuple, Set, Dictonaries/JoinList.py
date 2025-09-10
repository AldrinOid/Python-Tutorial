# join a list
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [True, False, True]

# using + operator
list4 = list1 + list2 + list3
print("Using + operator:", list4)

# using extend function
list1.extend(list2)
list1.extend(list3)
print("Using extend function:", list1)

# using append function in a loop
list5 = []
for item in list2:
    list5.append(item)
for item in list3:
    list5.append(item)
print("Using append function in a loop:", list5)
