def list_comprehensions():
    animals1 = ["dog", "cat", "rat", "rabbit"]

    animals2 = animals1.copy()
    print(id(animals1))
    print(id(animals2))
    print()

    # Creating a new list "animals3" using existing list "animals2"
    animals3 = [animal for animal in animals2]
    print(animals3)
    print()

    # Creating a new list "animals4" using existing list "animals3" + converting list elements into upper case letters
    animals4 = [animal.upper() for animal in animals3]
    print(animals4)
    print()

    # Assigned all elements in animals4 to animal
    # then getting the lenght of each element in list using len(animal) method
    # and then assigning new list 
    animals5 = [len(animal) for animal in animals4]
    print(animals5)
    print()

    # Multiplying each element to itself from list animals5
    # and assigning it to new list
    animals6 = [x*x for x in animals5]
    print(animals6)
    print()


def main():
    list_comprehensions()

main()