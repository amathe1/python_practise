

def main():
    # declaing a dictionary (key value pairs)
    # Dictonaries are ordered, they will stay where you put
    # Keys can be anything but should be immutable (should not use list as ket because they are mutable)
    fruits = { 1 : "Mango", 2 : "Apple", 3 : "Banana", True : "PineApple" }
    print(type(fruits))
    print()


    print(fruits[1])
    print(fruits[2])
    print(fruits[3])
    print(fruits[True])


    

main()