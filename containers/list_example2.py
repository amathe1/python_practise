"""
Given a list of integer values, write a Python program to check whether the list contains the same number in adjacent positions. Display the count of such adjacent occurrences.

Sample Input                        Output 
[1,1,5,100,-20,-20,6,0,0]               3
[10,20,30,40,30,20]                     0
[1,2,2,3,4,4,4,10]                      3

"""

def adjacent_positions(list):
    count = 0
    for i in range(len(list) - 1):
        if list[i] == list[i+1]:
            count += 1
    return count

def main():
    list = [1,1,1,5,100,-20,-20,6,0,0]
    count = adjacent_positions(list)
    print("No of occurences where adjascent values are equal are : ", count)

if __name__ == "__main__":
    main()
