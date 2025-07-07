items = {"pen", "book", "pencil"}

# add() => adding element into a set
items.add("eraser")
items.add("Pen")
print(items)
# Output : {'eraser', 'book', 'pen', 'pencil', 'Pen'}

# discard() => removing element from a set
items.discard("Pen")
print(items)
# Output : {'pen', 'book', 'eraser', 'pencil'}

# pop() => Removes and returns a random set element. 
# Raises KeyError if the set is empty.
items.pop()
print(items)
# Output : {'pencil', 'eraser', 'pen'}

# clear() => Removes all elements from set
items.clear()
print(items)
# Output : set()

# union() => Returns the union of two sets as a new set.
items1 = {"Apple", "Mango"}
items2 = {"Banana", "Grape"}
items3 = items1.union(items2)
print(items3)
# Output : {'Grape', 'Banana', 'Mango', 'Apple'}

# intersection() => Returns the common elements of two sets as a new set.
items1 = {'A', 'B', 'C'}
items2 = {'A'}
items3 = items1.intersection(items2)
print(items3)
# Output : {'A'}

# difference() => Returns the elements that are present in the first 
# set but not in the second set.
items1 = {"Red", "White", "Green"}
items2 = {"Red", "White"}
items3 = items1.difference(items2)
print(items3)
# Output : {'Green'}

# symmetric_difference() => This function returns the elements that are present 
# in either of the sets but not in both the sets.
Items1 = {"Carrot", "Chilly", "Pepper"}
Items2 = {"Carrot", "Chilly", "Pepper", "orange"}
Items3 = Items1.symmetric_difference(Items2)
print(Items3)
# Output : {'orange'}