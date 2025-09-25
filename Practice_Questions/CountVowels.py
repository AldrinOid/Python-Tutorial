given_text = input("Enter any text: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vowel_count = {vowel: 0 for vowel in vowels}
for char in given_text:
    if char in vowel_count:
        vowel_count[char] += 1
for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count} time(s)")


