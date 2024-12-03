"""
Write to check a palindrome

"""

def is_palindrome(strr1):
    strr2 = strr1[::-1]
    return strr2

def main():
    strr1 = input("Please enter a plaindrome : ")
    reverse_strr = is_palindrome(strr1)

    if strr1 == reverse_strr:
        print("Entered word is palindrome!")
    else:
        print("Entered word in not palindrome")


main()