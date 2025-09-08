def isPalindrome (str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            print(f"The {str} is not a palindrome")
            return False
    print(f"The {str} is a palindrome")
    
isPalindrome("racecar")    
isPalindrome("hello")
isPalindrome("energye")