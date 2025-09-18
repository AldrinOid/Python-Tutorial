# using try and except to catch errors

'''
Try = put risky code in here
Except = what to do if there is an error in the try block
Else = what to do if there are no errors in the try block (optional)
Finally = code that will run no matter what, regardless of the result of the try and except blocks (optional)

'''
x = 10
try: 
    print(x)
except:
    print("An error occurred")

# using try and except to catch specific errors
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# using else to run code when there is no error
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# using finally to run code regardless of the result of the try- and except blocks
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
