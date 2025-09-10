# unpacking item in the tuple
thistuple = ("apple", "banana", "cherry")
(green, yellow, red) = thistuple
print(green)
print(yellow)
print(red)

# unpacking with *
thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = thistuple
print(green)
print(yellow)
print(red)

