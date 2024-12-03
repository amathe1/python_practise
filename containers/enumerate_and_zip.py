

def main():

    fruits = ["Apple", "Mango", "Avacado"]
    animals = ["Dog", "Cat", "Rabbit"]
    members = ["Arun", "Anu", "Wine"]

    for i, fruit in enumerate(fruits):
        print(i, fruit)

    print()
    
    for fruit, animal in zip(fruits, animals):
        print(fruit, animal)

    print()

    for fruit, animal, member in zip(fruits, animals, members):
        print(fruit, animal, member)


main()