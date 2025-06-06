"""
Write a Python function, find_sum() that accepts an integer n and returns the sum of first n numbers. 
Invoke the function and display the sum of first n numbers.
"""

def find_sum(strr):
    list_of_number = list(map(int, strr.strip()))
    sum_of_given_no = sum(list_of_number)
    return sum_of_given_no

def main():
    number = input("Please enter a number : ")
    sum_of_given_no = find_sum(number)
    print("Sum of give number is : ", sum_of_given_no)

main()