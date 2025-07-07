"""
When you want to treat some data as a group, it would not be good to create individual variables for each data. 
You can store them together as a collection.
There are many collection data types which are supported by Python.

1. Tuple
2. List
3. Set
4. Dictionary


In a program, not all values are numerical. You also have alphabetical or alpha numerical values. 
Such values are called strings.

Example:"Hello World", "AABGT6715H" 

Each value in a string is called a character. 
Just like list elements, you can access the characters in a string based on its index position.

String         : "AABGT6715H"
Character      :  A, A, B, G, T, 6, 7, 1, 5, H
Index          :  0  1  2  3  4  5  6  7  8  9   

In Python, string is a data type and anything enclosed in a single quote or double quote is considered to be a string. 
All the remaining operations are similar to lists. But like tuples, strings are also IMMUTABLE.

String data type in Python has many inbuilt functions which makes it easier to work with strings.
Consider the string, name="Raghav".

"""

# STRING

name = "Raghav"

# Returns the count of a given set of characters. Returns 0 if not found
print(name.count('a'))
# Output : 2

# Returns a new string by replacing a set of characters with another set of characters. 
# It does not modify the original string
print(name.replace('a', 'A'))
# Output : RAghAv

# Returns the first index position of a given set of characters
print(name.find('a'))
# Output : 1

# Checks if a string starts with a specific set of characters, returns true or false accordingly.
print(name.startswith('Ra'))
# Output : True

# Checks if a string ends with a specific set of characters, returns true or false accordingly.
print(name.endswith('ar')) 
# Output : False

# Checks if all the characters in the string are numbers, returns true or false accordingly.
print(name.isdigit())
# Output : False

# Converts the lowercase letters in string to uppercase
print(name.upper())
# Output : RAGHAV

# Converts the uppercase letters in string to lowercase
print(name.lower())
# Output : raghav

# Splits string according to delimiter and returns the list of substring. Space is considered as the default delimiter.
print(name.split('a'))
# Output : ['R', 'gh', 'v']



# Example for understanding string methods in Python

boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))
if(boarding_call.find("AL"))>=0:
    print("Welcome to Air Lines.")
if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")
a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")
print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
message="Thank you all..Have a nice journey!"
print(message.upper())
print(message.lower())


# Output :
"""
Good Morning, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M.
Welcome to Air Lines.
Passengers are requested to have their breakfast.
Flight Number is specified to the passengers.
Total number of times flight service name is specified in the boarding call: 2
THANK YOU ALL..HAVE A NICE JOURNEY!
thank you all..have a nice journey!
"""







#  F String

"""
One of the most useful features of Python is the f-string. 
This new way of formatting strings lets you use embedded Python expressions inside string constants. 
Here is a simple example:
"""
name = "Stark"
print(f"He said his name is {name}.")
# Output : He said his name is Stark.

"""
You can put any Python expression inside the braces and it will be converted to a string 
and inserted into the string at that location. 
Notice that the expression is evaluated at run time and inserted into the string. This allows you to do things like this:
"""

width = 10
height = 20
print(f"The perimeter of the given rectangle is {(2 * width) + (2 * height)} and the area is {width * height}.")
# Output : The perimeter of the given rectangle is 60 and the area is 200.






# R String

"""
Another new feature of Python is the r-string, which is a string that is marked as a raw string by prefixing it with an r. 
This means that backslashes are treated as literal characters and not as escape characters. 
This is useful for regular expressions and Windows paths, which use backslashes a lot. Here's an example:
"""

print(r"C\\Users\\Stark\\Documents\\Books\\Python")
# Output : C\\Users\\Stark\\Documents\\Books\\Python






# Example to understand more about strings

# Creating a string
pancard_number="AABGT6715H"

# Length of the string
print("Length of the PAN card number is : ", len(pancard_number))
# Output : Length of the PAN card number is :  10

#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)
# Output : PAN card

# Iterating the string using range()
for index in range(0, len(pancard_number)):
    print(pancard_number[index])

# Iterating the string using value
for value in pancard_number:
    print(value)
    
# Sreaching for a charecter in string
if 'z' in pancard_number:
    print("Charecter is present")
else :
    print("Charecter is not present")
    
# Slicing a string
print("The numbers in the PAN car number : ", pancard_number[5: 9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])

# pancard_number[2] = 'A'
# This line will through an error, string is immutable
# Output : TypeError: 'str' object does not support item assignment


"""
Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number where,

Consider AL1 as the value for airline

src and dest should be the first three characters of the source and destination cities.

number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list of all generated ticket numbers.

"""

def generate_ticket(airline,source,destination,no_of_passengers):
    # Creating a list to append tickets numbers
    ticket_number_list = []
    # We need a variable 'i' to increment it everytime we appended a ticket number into above list
    i = 0
    # First condition (if no_of_passengers < 5)
    if no_of_passengers < 5:
        # Starting a loop to repeat until no_of_passengers == 0
        while no_of_passengers != 0:
            ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(101+i))
            # Incrementing count after adding a ticket number into list, it is to add this number into str(101+i)
            i = i+1
            # Decrementing no_of_passengers everytime we add a ticket into list
            # Making sure to -1 from 'no_of_passengers' everytime it looped in while condition
            no_of_passengers = no_of_passengers - 1
    else:
        for i in range(5):
            ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100+no_of_passengers))
            i = i+1
            no_of_passengers = no_of_passengers - 1
        ticket_number_list = ticket_number_list[::-1]

    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",10))

# Output :
# ['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108', 'AI:Ban:Lon:109', 'AI:Ban:Lon:110']



# =========================================================================================================================
#                                                   TUPLE
# =========================================================================================================================

"""
Suppose it is mandatory to have the following types of food in the lunch menu of the passengers.

Welcome Drink, Veg Starter, Non-Veg Starter, Veg Main Course, Non-Veg Main Course, Dessert

How to store it such that no one can modify the elements?

Of course, you can use a list but anybody can modify an element in the list. 
This is where you can use another collection data type known as tuple.

Like list, tuple can also store a sequence of elements but the value of the individual elements cannot be changed. 
(i.e. tuples are IMMUTABLE). Elements can be homogeneous or heterogeneous but, they are READ-ONLY.

"""

# Creating a Tuple
lunch_menu=("Welcome Drink","Veg Starter","Non-Veg Starter","Veg Main Course","Non-Veg Main Course","Dessert")
# () are optional, a set of values separated by comma is also considered to be a tuple.

sample_tuple="A","B","C"
# Although () are optional, it is a good practice to have them for readability of code.

# If we need to create a tuple with a single element, then we need to include a comma as shown below:
sample_tuple=("A",)


# Random write
# This will result in an error as tuple is immutable. Hence random write is not possible in tuple.
# lunch_menu[0] = ""

# tuple iteration
for element in lunch_menu:
    print(element)
    
# tuple slicing
tuple1 = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
# Forward slicing : 0,  1,  2,   3,  4,  5,  6, 7
# Reverse slicing : -8, -7, -6, -5, -4, -3, -2, -1

print(tuple1[0:7]) # ('A', 'B', 'C', 'D', 'E', 'F', 'G') ==> it will always do -1 from end index
print(tuple1[:7])  # ('A', 'B', 'C', 'D', 'E', 'F', 'G') ==> it start index is empty, then it will start from index 0
print(tuple1[:])   # ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H') ==> if end index is empty, it will consider last element as well

print(tuple1[:-1]) # ('A', 'B', 'C', 'D', 'E', 'F', 'G') ==> same in reverse slicing as well, it will do -1 from end index
print(tuple1[-5:-1]) # ('D', 'E', 'F', 'G') 

# Unpacking tuples 
elements = (True, 3.2, 7, "goat")

(is_raining, weight, volume, animal) = elements

print(is_raining)
print(weight)
print(volume)
print(animal)
print()


fruits = ("Mango", "Banana", "Apple", "Orange", "Grapes")

(fruit1, fruit2, fruit3, *multple_fruits) = fruits

print(fruit1)
print(fruit2)
print(fruit3)
print(multple_fruits)
print(type(multple_fruits)) # It will be a type of List






# =========================================================================================================================
#                                                   List
# =========================================================================================================================

"""
Let us start by exploring one of the most common collection data type - list. 
List can be used to store a group of elements together in a sequence. 
If you want to store the ticket numbers allocated to each passenger traveling in a flight, 
instead of using separate variables for each ticket number, you can use a list as shown below.
"""

# In case of having different variables for each ticket number, variables will be stored in separate memory locations. 
# Whereas in case of list, the elements will be stored in contiguous memory locations as illustrated below.
tickets_list = [101, 102, 103, 104]

"""
Each element in the list has a position in the list known as an index. 
The list index starts from zero. It is like having seat numbers starting from 0.

Element : 101    102     103     104 
Index   :  0      1       2        3

Index positions actually help us to directly access a value from the list.

list_name[index] can be used to directly access the list element at the mentioned index position.

If you want to allocate a different passenger to seat number 3, you can do it as ticket_list[3]=13504. 
Thus, in addition to using the index to access an element directly, 
you can also use it to directly modify an element in the list.

Just like how you cannot allocate 101st seat to a passenger in a 100 seat plane, 
you cannot access values beyond the total number of elements in the list.

For example: print(ticket_list[5]) will result in index out of bound error.
"""

# Let us see how to create a list in Python and perform some operations on it

# Creating an empty list
list1 = []
list2 = list()

# Creating a list with known size and known elements
# List can store both homogeneous and heterogeneous elements

sample_list1=["Mark",5,"Jack",9, "Chan",5]
sample_list2=["Mark","Jack", "Chan"]

# Creating a list with known size and unknown elements
# None denotes an unknown value in Python
sample_list=[None]*5

# Length of list :
# Displays the number of elements in the list
len(sample_list)

# Random access of elements :

# Random read
print(sample_list1[1])

# Random write
# List is mutable i.e., the above statement will rewrite the existing value at index position 2 with “James”.
sample_list[2]="James"

# Other operations on the list :

# Adding element at end of the list, list need not have a fixed size, it can grow dynamically
sample_list2.append("Arun")
print(sample_list2)


# Concatenating 2 lists :
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

print(id(l1))
print(id(l2))

# l1+=l2, concatenates l1 to l2
l1+= l2
print(l1)

# l1=l1+l2, creates a new list named l1 containing the concatenated elements from the original l1 and l2 
# Observe this difference while visualizing using id()
l1 = l1 + l2
print(l1)



# As elements are stored sequentially in a list, you can use a loop to access these elements :
list_of_airlines=["AL1","AL2","AL3"]
print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])
print("Iterating the list using keyword in")
for airline in list_of_airlines:
    print(airline)

# If you just want to find out whether an element is there in a list or not, you need not iterate through the list. 
# Instead you can check using if..in syntax. Try out the code and observe the results.
list_of_airlines=["AL1","AL2","AL3"]
airline="AL3"
if airline in list_of_airlines:
    print("Airline found")
else:
    print("Airline not found")





# List Slicing :

"""
Assume that the names of the airlines operating from an airport are stored in a list as shown below.
Suppose, you need to extract the airlines from the 1st to the 3rd index positions in the list. How can we do that?

List of Airline :   AL1     AL2     AL3     AL4     AL5
Index           :   0       1       2       3       4
Negative Index  :   -5     -4       -3     -2      -1

"""
# Python offers a simple solution in the form of slicing:
sub_list=list_of_airlines[1:4]
#The above line provides a sub-list from index position 1 to 3. That is, from 1 to (4-1). 
"""
For example: To fetch the second last airline in the list, you can write list_of_airlines[-2]. 
This is equivalent to list_of_airlines[len(list_of_airlines)-2]. 

Indices may also be considered negative as shown above. This is normally used to count from right. 
Negative indices can also be used for slicing.

For example: list_of_airlines[-4:-1] will give us the same output as list_of_airlines[1:4]
"""


# List datatype in Python has many inbuilt functions
# Consider a list 
num_list = [10, 20, 30, 40, 50]

num_list.append(60)
print(num_list)
# O/p : [10, 20, 30, 40, 50, 60]
# Adds an element to end of list

print(num_list.index(10))
# O/p : 0
# Returns the index position of the element.
# In case of multiple occurrences of the element, returns the index of the first occurrence.
# Throws ValueError, if the element is not found

num_list.insert(6,70)
print(num_list)
# Inserts an element at a given position

# list before pop :  [10, 20, 30, 40, 50, 60, 70]
print(num_list.pop(3))
print(num_list) # [10, 20, 30, 50, 60, 70]
# O/p : 40
# Removes and returns the element at given index position from the list

num_list.remove(10)
print(num_list)
# O/p : [20, 30, 50, 60, 70]
# Removes the first occurring element whose value is 10

num_list.sort()
# List will be sorted in ascending order

num_list.reverse()
print(num_list) # [70, 60, 50, 30, 20]
# Reverse the list




# Given a list of integer values, write a Python program to check whether the list contains 
# the same number in adjacent positions. Display the count of such adjacent occurrences.

"""
Sample Input                        Output 
[1,1,5,100,-20,-20,6,0,0]           3
[10,20,30,40,30,20]                 0
[1,2,2,3,4,4,4,10]                   3
"""

list_1 = [1,2,2,3,4,4,4,10]

counter = 0

for index in range(0, len(list_1)-1):
    if list_1[index] == list_1[index+1]:
        counter += 1

print(counter)


# List comprehension :
# This concept is useful while creting long lists based on a condition
animals1 = ["dog", "cat", "rat", "rabbit"]

animals2 = animals1.copy()
print(id(animals1))
print(id(animals2))
print()

# Creating a new list "animals3" using existing list "animals2"
animals3 = [animal for animal in animals2]
print(animals3)
print()

# Creating a new list "animals4" using existing list "animals3" + converting list elements into upper case letters
animals4 = [animal.upper() for animal in animals3]
print(animals4)
print()

# Assigned all elements in animals4 to animal
# then getting the lenght of each element in list using len(animal) method
# and then assigning new list 
animals5 = [len(animal) for animal in animals4]
print(animals5)
print()

# Multiplying each element to itself from list animals5
# and assigning it to new list
animals6 = [x*x for x in animals5]
print(animals6)
print()

numbers1 = [x for x in range(0,20)]
print(numbers1)
print()

numbers2 = [x for x in numbers1 if x > 5]
print(numbers2)
print()

numbers3 = [x for x in numbers1 if  x % 2 != 0]
print(numbers3)
    
    
    
    
    
# =========================================================================================================================
#                                                   Set
# =========================================================================================================================

"""
In python sets are used to store unique elements. 
They are similar to array in terms of appearance, however they do not allow duplicate elements. 
Sets also sets support mathematical operations like union, intersection, difference, etc.
"""

# To create a set with 3 elements
Items = {"Carrot", "Chilly", "Pepper"}
print(Items)
# O/p : {"Carrot", "Chilly", "Pepper"}

# To create an empty set
visited = set()
print(visited)





# SET FUNCTIONS

# Adding an element 
Items.add("Beans")
print(Items)

# Deleting an element
Items.discard("Pepper")
print(Items)

# Difference betwen pop() & clear()

# Removes and returns a random set element. Raises KeyError if the set is empty.
Items.pop()
print(Items)

# Removes all elements from the set.
Items.clear()
print(Items)


# Difference between union() & intesection()

# union() returns the union of two sets as a new set
Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.union(Items2)
print(Items3)
# O/p : {‘Carrot’, ‘Chilly’, ‘Pepper’, ‘orange’}C

# intersection() returns the common elements of two sets as a new set
Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.intersection(Items2)
print(Items3)
# O/p : {‘Carrot’, ‘Chilly’, ‘Pepper’}C

# difference() - Returns the elements that are present in the first set but not in the second set.
Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.difference(Items2)
print(Items3)
# O/p : set()

# symmetric_difference() - This function returns the elements that are present in either of the sets but not in both the sets.
Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.symmetric_difference(Items2)
print(Items3)
# O/p : {'orange'}





# =========================================================================================================================
#                                                   Dict
# =========================================================================================================================

"""
A dictionary can be used to store an un-ordered collection of key-value pairs.

The key should be unique and can be of any data type.

Like lists, dictionaries are muttable.

"""

# Creating a dictionary
fruits = {1 : "Mango", 2 : "Orange", 3 : "Grape"}
# First element in every pair is the key and the second element is the value.

# Accessing the value using key
print(fruits[3])
# This will return the corresponding value for the specified key

# Iterating through dictionary
# items() function gives both key and value, which can be used in a for loop
for key, value in fruits.items():
    print(key, value)