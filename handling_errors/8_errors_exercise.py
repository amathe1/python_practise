"""

Write a function to convert feet to miles.

(miles = feet * 1.89E-4)

Using this function, write a program to ask the user to enter a distance in feet and convert it to miles.

If the user enters valid input, print the distance in miles to three decimal places and quit.
If the user enters invalid input, print "Invalid input" and ask them again.

If the uer enters "quit", quit the program.

Mount everest is 29,028 feet high. How high is it in miles ?

"""

import re

def feet_to_miles(feet):
    return feet * 1.89E-4


def main():
    while True :
        feet = input("Enter the distance >")

        if feet == "quit":
            break
        
        try:
            feet = re.sub(",", "", feet)
            #feet = feet.replace(",", "")
            miles = feet_to_miles(int(feet))
            print(f"{feet} in feet is {miles:.3f} in miles")
            break
        except:
            print("Invalid input")

main()