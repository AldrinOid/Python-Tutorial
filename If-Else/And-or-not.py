# using and in condition
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")

# using or in condition
a = 3
b = 8
if a > 5 or b > 5:
    print("At least one condition is true")

# using not in condition
c = 7
if not c > 10:
    print("c is not greater than 10")

# combining and, or, and not
m = 4
n = 12
if (m > 5 and n > 10) or not (m < 3):
    print("Complex condition is true")

# using if-elif-else with and, or, not
p = 6
if p > 10:
    print("p is greater than 10")
elif p > 5 and p <= 10:
    print("p is between 6 and 10")
else:
    print("p is 5 or less")

# using shorthand if with and, or, not
q = 9
print("q is greater than 5 and less than 10") if q > 5 and q < 10 else print("q is not in the range")