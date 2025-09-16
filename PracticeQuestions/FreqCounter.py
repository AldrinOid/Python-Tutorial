given_string = input("Enter any phrase:  ")

given_text = given_string.split()

word_count = {word: 0 for word in given_text}
for word in given_text:
    word_count[word] += 1
for word, count in word_count.items():
    print(f"{word}: {count} time(s)")

