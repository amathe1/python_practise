fruits1 = { 
        "Apple" : "Green", 
        "Orange" : "Orange", 
        "Banana" : "Yellow" 
        }

fruits2 = fruits1.copy()

fruits1.pop("Apple")

print(fruits1)
print(fruits2)

# fruits2.items() will return a tuple
# we have to unpack them in key, value and pass it to new dict() fruits3
fruits3 = {key:value for (key,value) in fruits2.items()}

print()
print(fruits3)