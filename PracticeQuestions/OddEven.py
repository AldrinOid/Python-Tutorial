def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    elif number % 2 != 0:
        print(f"{number} is an odd number.")
    else:
        print("Invalid input. Please enter a valid integer.")
    return 0

input_number = int(input("Enter a number: "))
check_odd_even(input_number)