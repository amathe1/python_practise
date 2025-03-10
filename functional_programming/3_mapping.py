"""
In python, map() is a built in function that allows you to apply a given function to all items in the iterable.

map() is useful for applying a function to each item of an iterable without needing to explicitly loop through the items.

Syntax :
map(function, iterable)


"""

def square(n):
    return n * n

def add(x, y):
    return x + y

def main():
    list_of_numbers = [1, 2, 3, 4, 5]
    # Example1 with one function and one iterable
    result1 = map(square, list_of_numbers)
    print(list(result1))

    list1 = [10, 20, 30]
    list2 = [10, 20, 30]

    # Example2 with one function and two iterables
    result2 = map(add, list1, list2)
    # The map() function returns a map object, which is an iterator. 
    # To see the results, you need to convert it to a list or loop through it.
    print(list(result2))


if __name__ == "__main__":
    main()

