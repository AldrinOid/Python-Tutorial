def divide_by(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")
        return 0

ans = divide_by(10, 0)  # This will raise a ZeroDivisionError
print(ans)  # Output will be 0 due to the exception handling