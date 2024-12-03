"""

Write a function that calculates pi

You can calculate PI by adding up a large number of terms of the following series :

pi = 4 * (1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ...)

You can check your value against the actul value of PI. 
Import the math module and then use math.pi

"""
import math

def calculate_pi():
    

    sum = 0.0
    value = 1
    sign = 1

    # sum is the total value
    # value will be incremented by 2 every time it loop
    # Note w assigned sign = 1 (+ve number), then multiplying it with '-1' everytime it goes into loop, that will give 1, -1, 1, -1 in a loop
    # finally we are adding 'sum' to itself multiplied by 1/value "sum = sum + sign * 1/value"
    for i in range(0, 10000):
        sum += sign * 1/value
        value += 2 
        sign *= -1
    return 4 * sum

def main():
    print("Calculated PI value : ", calculate_pi())

    print ("PI value as per math.pi : ", math.pi)
    

main()