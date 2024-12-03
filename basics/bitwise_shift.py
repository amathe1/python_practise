"""
Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and returns value of the integer num rotated to the right by n positions. Assume both the numbers are unsigned. Invoke the function and print the return value.

Hint: use >> binary operator to shift the bits.

Example: num=60, n=2 result=15
"""

# Right shift is always like divisible by 2
# Given number is 60
# If we right shift once then, 60/2 = 30, again one more right shift, 30/2 = 15

# Left shift would be multiplied for 2
# If we left shift once, then 60 * 2 = 120, if we left shift again, then 120 * 2 = 240

def right_shift(num, n):
    return num >> n

def main():
    num = 60
    n = 2

    value = right_shift(num, n)
    print(value)


main()
