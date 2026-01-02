
"""
Tuples : Immutable

"""

def main():
    # Defining a Tuple 
    animals = ("cat", "dog", "wolf", "tiger")
    print("Type of above Tuple is : ",type(animals))

    print()
    print("One way of looping the Tuple 'animals' :")
    for animal in animals:
        print(animal)
    
    print()
    print("Another way of looping the Tuple 'animals' :")
    for i in range(0, len(animals)):
                   print(animals[i])

    
    print()
    print("We are just changing the reference of a Tuple as below :")
    print('tuple_1 = ("B", "A", "D")')
    print('tuple_1 = ("X") ')
    print('print(tuple_1) ')
    tuple_1 = ("B", "A", "D")
    print(id(tuple_1))
    tuple_1 = ("X") 
    print(id(tuple_1))
    print(tuple_1) 




main()