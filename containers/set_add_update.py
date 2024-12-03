
def set_add_update():
    numbers1 = {1, 2, 3, 4, 5}
    print(numbers1)
    print()

    # Usig add() method
    numbers1.add(6)
    numbers1.add(7)
    print(numbers1)
    print()

    # Using update() method
    numbers2 = {8, 9, 10}
    numbers1.update(numbers2)
    print(numbers1)
    print()

    numbers3 = ["cat", "dog", 20, 30, 40, 3.5]
    numbers1.update(numbers3)
    print(numbers1)


def main():
    set_add_update()

main()