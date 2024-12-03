def extended_slicing():
    numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    #print(numbers[0:10:2])

    print(numbers[3:10:2])
    print()

    # If start, end not mentioned in slicing then default will be first & last in actual list 
    print(numbers[:])
    print()

    # If range not mentioned, then default will be "1"
    print(numbers[::1])
    print()

    gretting = "Hello there!"
    print(gretting[1:4])
    print()

    # String mentioned inside print is a string arguments and use can use slicing for this string
    print("What are you?"[3::3])


def main():
    extended_slicing()


main()