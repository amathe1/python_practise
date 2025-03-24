"""

We need to use pickle module to dump and load objects into/from a file


"""

from pickle import dump, load

def main():
    # Creating 3 objects ; list, string, dict
    numbers = [1.2, 3.23, 4.34, 2.33]
    text = "Hello ! How are you today!"
    lookup = {

        1: "Jan",
        2: "Feb",
        3: "Mar"
    }

    # Creating a file to dump above objects
    filename = "/Users/Arunkumar_Mathe/Documents/python_practise/files/data.bin"

    # Opening file to dump objects
    with open(filename, 'wb') as file:
        dump(numbers, file)
        dump(text, file)
        dump(lookup, file)

    # deleting objects after loading into file 
    del numbers
    del text
    del lookup

    # opening the file to load objects from file
    with open(filename, 'rb') as file:
        numbers = load(file)
        text = load(file)
        lookup = load(file)
    
    print(numbers)
    print(text)
    print(lookup)


if __name__ == "__main__":
    main()