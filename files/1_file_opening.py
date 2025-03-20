"""

1. Opening a file
2. Reading all lines
3. Printing all lines

"""

def main():
    file = open(r"/Users/Arunkumar_Mathe/Documents/python_practise/files/asl1.csv")
    lines = file.readlines()
    for line in lines:
        print(line, end="")
    file.close()

if __name__ == "__main__":
    main()