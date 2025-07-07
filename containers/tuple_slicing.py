def main():
    numbers = ("One", "Two", "Theee", "Four", "Five")
    # Printing partial elements based on index
    # Both [0:4] & [:4] is same, if you don't mention start index, default is 0
    print(numbers[0:4])
    print(numbers[:4])
    print()
    print(numbers[1:3])
    print()

    print(numbers[-1])
    print(numbers[-2])
    print(numbers[-3])
    print(numbers[-4])
    print(numbers[-5])
    print()
    # Reverse slicing, -1 is last element in list, followed by -2, -3 towards left to right
    # In reverse slicing, if you mention [:-1], it will ignore last element and print rest
    print(numbers[:-1])
    print(numbers[-5:-1])
    print()

    text = "It was a good move"
    print(text[0:6])
main()