"""

Serialization       : Turn data into a series of bytes
De-Serialization    : Turn data series of bytes back into data type 

"""

def main():
    filename = r"/Users/Arunkumar_Mathe/Documents/python_practise/files/arun.bin"

    data = b'Hello'

    with open(filename, 'wb') as file:
        file.write(data)

    with open(filename, 'rb') as file:
        result = file.read(5)
        print(result)

if __name__ == "__main__":
    main()