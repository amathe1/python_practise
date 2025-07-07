"""
List data type in Python has many inbuilt functions.

"""

num_list = [10, 20, 30, 40, 50]

# append() => Add element to end of list
num_list.append(60)
print(num_list)
# Output : [10, 20, 30, 40, 50, 60]

# index() 
#       - Returns the index of given elements
#       - Returns the indes of first occurence, incase of multiple occurences
#       - Return a ValueError, if the element is not found
print(num_list.index(10))

# insert() => Insert the element at a given position
# List before insert() : [10, 20, 30, 40, 50, 60]
num_list.insert(3, 35)
print(num_list)
# List after insert() : [10, 20, 30, 35, 40, 50, 60]

# pop() => Removes and returns the element at given index position from the list
num_list.pop(3)
print(num_list)
# List after pop() : [10, 20, 30, 40, 50, 60]

# remove() => Removed the first occurence element
num_list.remove(60)
print(num_list)
# List after remove() : [10, 20, 30, 40, 50]

# sort() => Sorts the list in ascending order
num_list2 = [5, 4, 6, 7, 2, 1, 9, 8, 3, 10]
num_list2.sort()
print(num_list2)
# List after sort : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# reverse()
num_list2.reverse()
print(num_list2)
# List after reverse() : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]