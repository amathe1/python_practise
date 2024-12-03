
def main():
    
    numbers = [ [1,2,3], [4,5,6], [7,8,9]  ]

    #print(numbers)
    #print(type(numbers))

    sublist = numbers[0]
    #print(sublist)
    #print(type(numbers))

    # This is a 2 dimensional list
    print(numbers[2][0])

    # Looping a 2 dimensional list : First way
    for list in numbers:
        for sublist in list:
            print(sublist, end=" ")
        print()

    print()

    # Looping a 2 dimensional list : Second way
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers[i])):
            print(numbers[i][j], end="\n")
        print()



main()