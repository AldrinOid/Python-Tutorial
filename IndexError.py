items = [1,2,3,4,5]

try:
    item = items[6]  # Attempting to access an index that doesn't exist
    print(item)  # This will raise an IndexError
except IndexError as e:
    print(f"An error occurred: {e}")

