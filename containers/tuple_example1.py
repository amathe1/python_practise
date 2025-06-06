"""
Suppose it is mandatory to have the following types of food in the lunch menu of the passengers.

Welcome Drink, Veg Starter, Non-Veg Starter, Veg Main Course, Non-Veg Main Course, Dessert

How to store it such that no one can modify the elements?

Of course, you can use a list but anybody can modify an element in the list. 
This is where you can use another collection data type known as tuple.

Like list, tuple can also store a sequence of elements but the value of the individual elements cannot be changed. 
(i.e. tuples are IMMUTABLE). Elements can be homogeneous or heterogeneous but, they are READ-ONLY.


"""

lunch_menu=("Welcome Drink","Veg Starter","Non-Veg Starter","Veg Main Course","Non-Veg Main Course","Dessert")

# () are optional, a set of values separated by comma is also considered to be a tuple.
# Although () are optional, it is a good practice to have them for readability of code.
sample_tuple="A","B","C"

# If we need to create a tuple with a single element, then we need to include a comma as shown below:
sample_tuple=("A",)

# This will result in an error as tuple is immutable. Hence random write is not possible in tuple.
lunch_menu[0]=""