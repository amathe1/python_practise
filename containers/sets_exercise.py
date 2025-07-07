"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

which cubic numbers are also square numbers ?
which cubic numbers are not square numbers ?

"""

def sets_exercise():
    cubic_numbers = {x**3 for x in range(1,20) if x*x*x <= 729}
    print("Cubic numbers are", cubic_numbers)
    print()

    square_numbers = {i**2 for i in range(1,50) if i*i <= 729}
    print("Square numbers are",square_numbers)
    print()

    # cubic numbers are also square numbers
    print(cubic_numbers.intersection(square_numbers))
    print()

    # cubic numbers are not square numbers
    print(cubic_numbers.difference(square_numbers))
    print()

def main():
    sets_exercise()

main()
