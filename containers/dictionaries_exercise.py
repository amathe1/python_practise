"""

Write a program that asks the user to enter a name.

If the user enters a name in the list below,  respond with the age
of the person entered. Otherwise print "Unknown person".

Make the program keep asking for the names like this until the user enters
"quit. Then the program exits.

Start by putting the names and ages in a dictionary.


"""

def main():
    people = ["Amelina", "Arthur", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
    age = [20, 30, 25, 65, 21, 70, 32, 45]

    dict1 = {
        "Amelina" : 20,
        "Arthur"  : 30,
        "Isla"    : 25,
        "Noah"    : 65,
        "Ava"     : 21,
        "Leo"     : 70,
        "Mia"     : 32,
        "Oscar"   : 45
     }
    
    do_loop = True

    while do_loop:
         person_name = input("Enter the name of the person : ")
         age = dict1.get(person_name)
         

         if person_name != "Quit":
            print("Age of the person mentioned by you is : ", age)
         else:
             do_loop = False
              


main()