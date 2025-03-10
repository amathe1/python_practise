

def main():
    # ord() will print the integer value of unicode point for given charecter
    print(ord('A'))

    # chr() will print the corresponding charecter as a string
    print(chr(65))

    # Printing the charecters from 'A' to 'Z' using chr() & ord()
    numbers = [chr(x) for x in range(ord('A'), ord('Z'))]
    print(numbers)

if __name__ == "__main__":
    main()