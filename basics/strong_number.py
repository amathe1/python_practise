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
    #print("List1 inside strong_number : ", list1)
    for i in range(0, len(list1)):
        list2.append(recursive(list1[i]))

    
    return list2

def recursive(num):
    if num == 0:
        return 1
    else:
        return num * recursive(num-1)

def main():
    final_list = []
    number = input("Please enter a number : ")
    list1 = list(map(int, number.strip()))
    final_list = strong_number(list1)
    sum_of_individual_numbers_factorial = sum(final_list)
    print(sum_of_individual_numbers_factorial)

    if int(number) == sum_of_individual_numbers_factorial:
        print("Given number is a string number")
    else:
        print("Given number is not a strong number")


main()