def main():
    elements = (True, 3.2, 7, "goat")

    (is_raining, weight, volume, animal) = elements

    print(is_raining)
    print(weight)
    print(volume)
    print(animal)
    print()


    fruits = ("Mango", "Banana", "Apple", "Orange", "Grapes")

    (fruit1, fruit2, fruit3, *multple_fruits) = fruits

    print(fruit1)
    print(fruit2)
    print(fruit3)
    print(multple_fruits)
    print(type(multple_fruits)) # It will be a type of List



main()