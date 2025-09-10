# access item in tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# negative indexing
print(thistuple[-1])

# range of indexes
print(thistuple[2:5])

# range of negative indexes
print(thistuple[-4:-1])

# check if item exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple")
if "pineapple" not in thistuple:
    print("No, 'pineapple' is not in the tuple")

# loop through a tuple
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

# join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# count items in a tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
y = thistuple.count(7)
print(y)
z = thistuple.count(8)
print(z)
a = thistuple.count(1)
print(a)
b = thistuple.count(3)
print(b)

# find index of an item
thistuple = (1, 2, 3, 4, 5, 6)
x = thistuple.index(4)
print(x)
y = thistuple.index(1)
print(y)
z = thistuple.index(6)
print(z)

# unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# unpack with *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
