# # without using slicing

def reverse_string(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text

input_word = input("Enter any word: ")
print(reverse_string(input_word))
