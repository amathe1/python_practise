def main():
    animals1 = ("Dog", "Cat", "Rabbit")
    animals2 = ("Tiger", "Elephant", "Fox")

    fruits1 = ["Mango", "Grapes", "Orange"]
    fruits2 = ["Papaya", "Apple"]

    # As tuples are immutable, we can't add 2 tuples, instead it will create a new tuple after adding above two tuples
    # Hence 2 different referece ID's will pointed to 2 different tuple objects
    print(id(animals1))
    # animals1 = animals1 + animals2 can be written as below
    animals1 += animals2
    print(animals1)
    print(id(animals1))

    print()

    # As lists are muttable, same reference ID will be retained and it will refer to same ref object after adding both lists
    print(id(fruits1))
    fruits1 += fruits2
    print(fruits1)
    print(id(fruits1))


main()