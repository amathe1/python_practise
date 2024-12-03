def insert_extend():

    animals = ["Elephant", "Fox", "Lion"]
   
    # insert() method will insert elements in a list
    animals.insert(1, "Monkey")

    print(animals)
    print()
    more_animals = ["Tiger", "Cheetah"]

    # extend() method add a new list to existing list
    animals.extend(more_animals)

    print(animals)

def main():
    insert_extend()

main()