"""

def factorial_solution(value):
    result = 1
    for i in range(2, value+1):
        result = result * i
    return result

def main():
    result = factorial_solution(10)
    print("Factorial of given value is", result)

main()

"""


# factorial of a number (applicable to only positive numbers)
# n! = n * (n - 1) * (n - 2) * .... 3 * 2 *1

# Ex : 5! = 5 * 4 * 3 * 2 * 1
# 5! = 120

# Factorial of zero is 1.
# 0! = 1 


def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)


def main():
    number = input("Please enter the number : ")
    number = int(number)

    if number < 0:
        print("Please enter a number greater than '0'")
    elif number == 0:
        print("factorial of zero is 1")
    else:
        print(f"Factorial of given number {number} is : ", recursive_factorial(number) )

main()















