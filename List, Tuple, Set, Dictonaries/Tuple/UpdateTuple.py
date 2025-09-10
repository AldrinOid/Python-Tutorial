# update a tuple

thistuple = (1, 2, 3, 4, 5)
y = list(thistuple)
y[1] = 10
thistuple = tuple(y)
print(thistuple)

# add items to a tuple
thistuple = (1, 2, 3)   
y = list(thistuple)
y.append(4)
thistuple = tuple(y)
print(thistuple)
