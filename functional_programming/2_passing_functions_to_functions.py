"""
we are passing a function func() to another function apply() in main() 


"""


def func(n):
    return n * 2

def apply(values, func):
    result = []

    for value in values:
        result.append(func(value))
    
    return result

def main():
    values = [1, 2, 3, 4, 5]

    final_result = apply(values, func)

    print(final_result)


if __name__ == "__main__":
    main()