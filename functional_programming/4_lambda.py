"""

Instead of writing a seperate method to square numbers, we can use lambda.



In Python, a lambda function is a small anonymous function defined using the lambda keyword. 
Unlike regular functions defined with def, a lambda function can have any number of arguments but only one expression. 
The expression is evaluated and returned when the function is called.

Syntax :
lambda arguments: expression



"""


def main():
    
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Using lambda with map()
    # Instead of writting separate function for expression, we can use lambda and write expression here itself
    result1 = map(lambda x : x * x, list1)
    print(list(result1))

    # Using lambda with filter()
    # Use filter when you have condition
    result2 = filter(lambda x : x % 2 == 0, list1)
    print(list(result2))

    


if __name__ == "__main__":
    main()