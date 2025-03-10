

def main():
    with open(r"D:\GitHub\Python\python_practise\files\asl1.csv") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")
            
    

if __name__ == "__main__":
    main()