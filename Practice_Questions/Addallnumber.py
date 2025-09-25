def add_all_numbers(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

# print(add_all_numbers(mylist))

input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("The sum of the entered numbers is:", add_all_numbers(input_list))