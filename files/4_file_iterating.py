
def main():
    with open(r"D:\GitHub\Python\python_practise\files\asl1.csv") as file:
        for line in file:
            print(line,end="")

if __name__ == "__main__":
    main()