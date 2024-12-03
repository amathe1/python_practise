"""
A prime number is a natural number which is greater than 1 and has no positive divisor other than 1 and itself, such as 2, 3, 5, 7, 11, 13, and so on.

The user is given two integer numbers, lower value, and upper value. The task is to write the Python program for printing all the prime numbers between the given interval (or range).

To print all the prime numbers between the given interval, the user has to follow the following steps:

Step 1: Loop through all the elements in the given range.
Step 2: Check for each number if it has any factor between 1 and itself.
Step 3: If yes, then the number is not prime, and it will move to the next number.
Step 4: If no, it is the prime number, and the program will print it and check for the next number.
Step 5: The loop will break when it is reached to the upper value.


"""

# First, we will take the input:  
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  

for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

