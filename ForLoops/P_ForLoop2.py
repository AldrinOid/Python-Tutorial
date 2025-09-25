color = ["red", "blue", "green"]

for i in range(len(color)):
    print("Index:", i, "Value:", color[i])

print('\n')
print('\n')

colors = ["red", "green", "blue"]
shapes = ["circle", "square"]

for i in range(len(colors)):          # outer loop
    for j in range(len(shapes)):      # inner loop
        print(i, j, colors[i], shapes[j])

'''
* So the outer loop will run only after the inner loop finishes its job. 
* like the inner loop will continue iterating if it reaches its limit, after that, the outer loop will run again

Think of the nested loops like a clock:

1. The outer loop is the hour hand.

2. The inner loop is the minute hand.

The minute hand (inner loop) goes all the way around before the hour hand (outer loop) moves to the next hour.

'''
print()

rows = 5
cols = 5

for i in range(1, rows + 1):  # outer loop → each row number
    for j in range(1, cols + 1):  # inner loop → each column number
        product = i * j
        # print each product with a fixed width so it lines up like a table
        print(f"{product:4}", end="")
    print()
# output: 
# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  15



print()

height = 5

for row in range(1, height + 1):
    for col in range(row):
        print("*", end="")
    print()
# Question: why in the for loop of col use the range(row)?
# Answer: the goal is to have each row print as many stars as the row number.


# output:
# *
# **
# ***
# ****
# *****

size = 6   # the board will be 6 rows by 6 columns

for row in range(size):  # outer loop → each row
    for col in range(size):  # inner loop → each column in that row
        # Print X if the sum of row and column indexes is even, else O
        if (row + col) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
# output: 
#     0 1 2 3 4 5
# 0 = X O X O X O
# 1 = O X O X O X
# 2 = X O X O X O
# 3 = O X O X O X
# 4 = X O X O X O
# 5 = O X O X O X

