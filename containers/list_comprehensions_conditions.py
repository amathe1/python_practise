def list_comprehensions_conditions():
    numbers1 = [x for x in range(0,20)]
    print(numbers1)
    print()

    numbers2 = [x for x in numbers1 if x > 5]
    print(numbers2)
    print()

    numbers3 = [x for x in numbers1 if  x % 2 != 0]
    print(numbers3)


def main():
    list_comprehensions_conditions()

main()