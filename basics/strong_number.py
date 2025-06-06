"""
Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True if the number is strong number else false. Invoke the function and based on return value print the number is strong number or not.

A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.

Example:145 is strong number as

1!=1

4!=24

5!=120

Sum of all these is 145

"""
def strong_number(list1):
    list2 = []
    # Looping all elements in list1 & converting a second list "list2" after applying recursive_fact() logic
    # Now, list2 will have the factorial numbers of elements from list1
    for i in range(0, len(list1)):
        list2.append(recursive_fact(list1[i]))

    
    return list2

def recursive_fact(num):
    if num == 0:
        return 1
    else:
        return num * recursive_fact(num-1)

def main():
    # Declaring a empty final list
    final_list = []
    
    # Asking user to enter a number
    number = input("Please enter a number : ")
    
    # Applying strip() to strip all numbers in integer
    # map((int, number.strip())) will covert all stripped numbers into integer type
    # list(map(int, number.strip())) will convert a list of numbers (so that we can find the factorial of each number)
    list1 = list(map(int, number.strip()))

    # Passing intial list to definition strong_number()
    final_list = strong_number(list1)

    # Calculating the sum of all factorials 
    sum_of_individual_numbers_factorial = sum(final_list)
    print(sum_of_individual_numbers_factorial)

    # if intial number is equal to sum of all factorial numbers then it is strong number
    if int(number) == sum_of_individual_numbers_factorial:
        print("Given number is a strong number")
    else:
        print("Given number is not a strong number")


main()