# using nested if-else statements

age = 25
if age < 18:
    print("You are a minor.")
else:
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    if score >= 50:
        print("Grade: C")
    else:
        print("Grade: F")

num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

# using nested if with shorthand if-else
a = 10
print("a is positive and even") if a > 0 and a % 2 == 0 else print("a is positive and odd") if a > 0 else print("a is not positive")
