def modifying_lists():
    fruits1 = ["Apple", "Mango", "Banana", "Grape", "MuskMelon"]

    fruits1.append("Papaya")
    fruits1.append("Guava")

    print(fruits1)

    # fruits1 = ['Apple', 'Mango', 'Banana', 'Grape', 'MuskMelon', 'Papaya', 'Guava']

    print()
    print(fruits1[1:3])

    print()
    print(fruits1[0:])

    print()
    fruits1[5:] = ["Lemon"]
    print(fruits1)


def main():
    modifying_lists()


main()