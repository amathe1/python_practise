"""
* List is mutable, we can add/delete values inside it
    
"""

"""
def main():
    # Declaring a tuple
    tuple = ("Apple", "Mango", "Orange")
    print(tuple)
    print(type(tuple))
    print()
   
   # Converting above tuple into list
    list1 = list(tuple)
    print(list1)
    print(type(list1))
    print()

    #Declating a list
    list2 = ["One", "Two", "Three"]
    for list_value in list2:
        print(list_value)
    

    #Slicing a list, it will start with list2[0] & it won't print last item
    print(list2[0:2])
"""

def main():
    list1 = [1, 2, 1, 2, 3, 4, 3, 4]
    #print(list(set(list1)))

    for item in list(set(list1)):
        print(item)


main()