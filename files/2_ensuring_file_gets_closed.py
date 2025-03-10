"""
Incase if any exception occur while reading the file in try block, 
finally will always execute and close the file


"""

def main():
    try:
        file = open(r"D:\GitHub\Python\python_practise\files\asl1.csv")
        lines = file.readlines()
        for line in lines:
            print(line, end="")
    finally:
        file.close()

if __name__ == "__main__":
    main()