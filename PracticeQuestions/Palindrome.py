def isPalindrome(word):
    startIndex = 0                  # start from the first letter
    endIndex = len(word) - 1        # start from the last letter

    while startIndex < endIndex:    # keep going until they meet
        if word[startIndex] != word[endIndex]:  # compare letters
            print(f"{word} is NOT a palindrome")
            return False
        startIndex += 1             # move forward from start
        endIndex -= 1               # move backward from end

    print(f"{word} IS a palindrome")
    return True
