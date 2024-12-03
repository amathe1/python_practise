def main():
    fruits = { "Apple" : "Green", 
              "Orange" : "Orange", 
              "Banana" : "Yellow" 
              }
    print()
    print(fruits)
    print()

    # Iterating through dictionaries
    for fruit in fruits:
        print(fruit + " : " + fruits[fruit])
    
    print()

    
    # Iterating through dict and printing only keys
    for fruit in fruits.keys():
        print(fruit)

    print()

    # Iterating through dict and printing only values
    for fruit in fruits.values():
        print(fruit)

    print()
    
    # This will print output in tuple type
    for fruit in fruits.items():
        print(fruit)
    
    print()

    # Same as above but unpacking incoming tuple and printing them 
    for fruit, color in fruits.items():
        print(fruit +" : " + color)



main()