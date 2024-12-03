def main():
    fruits = { 
        "Apple" : "Green", 
        "Orange" : "Orange", 
        "Banana" : "Yellow" 
        }
    
    print(fruits)

    del fruits["Apple"]

    print()
    print(fruits)
    print()

    color = fruits.pop("Banana")
    print(color)

    print()
    print(fruits)

main()