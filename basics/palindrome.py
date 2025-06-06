"""
Write to check a palindrome

Example :

string1 = "12321"
Reverse of this string is also same as itself. Hence it is palindrome.

"""

def is_palindrome(strr1):
    # This is a simple way to reverse a string
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