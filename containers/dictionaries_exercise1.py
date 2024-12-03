"""

Write a program that asks the user to enter a name.

If the user enters a name in the list below,  respond with the age
of the person entered. Otherwise print "Unknown person".

Make the program keep asking for the names like this until the user enters
"quit. Then the program exits.

Start by putting the names and ages in a dictionary.


"""

def create_lookup(people, ages):

    lookup = dict()

    #for i in range(0, len(people)):
    #    name = people[i]
    #    age  = ages[i]
    #    lookup[name] = age
    
    # Below code will zip 2 lists people, age and zipped it into a dict
    for name, age in zip(people, ages):
        lookup[name.casefold()] = age
    
    # print("=====>", lookup)
    # Output :
    # =====> {'amelina': 20, 'arthur': 30, 'isla': 25, 'noah': 65, 'ava': 21, 'leo': 70, 'mia': 32, 'oscar': 45}

    return lookup

def user_lookup(lookup):

    while True:
        name = input("Please enter the username : ")
        

        if name == 'quit':
            break
        
        age = lookup.get(name.casefold())

        if age is None:
            continue

   

        print(name + " is " + str(age) + " years old!")


def main():
    people = ["Amelina", "Arthur", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
    ages = [20, 30, 25, 65, 21, 70, 32, 45]

    lookup = create_lookup(people, ages)

    user_lookup(lookup)



main()