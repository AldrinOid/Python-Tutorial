# using while statement

i = 1
while i <= 5:
    print("My number is", i)
    i += 1


i = 10
while i > 0:
    print("I'm bigger number", i)
    if i == 3:
        break
    i -= 1

i = 0
while i < 6:
    i += 1
    if i == 3:
      continue
    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

