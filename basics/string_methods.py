
name = "Raghav"

# Returns the count of a given set of characters. Returns 0 if not found
print(name.count("a"))

# Returns a new string by replacing a set of characters with another set of characters. 
# It does not modify the original string
print(name.replace("a","A"))

# Returns the first index position of a given set of characters
print(name.find("a"))

# Checks if a string starts with a specific set of characters, returns true or false accordingly.
print(name.startswith("Ra"))

# Checks if a string ends with a specific set of characters, returns true or false accordingly.
print(name.endswith("ha"))

# Checks if all the characters in the string are numbers, returns true or false accordingly.
print(name.isdigit())

# Converts the lowercase letters in string to uppercase
print(name.upper())

# Converts the uppercase letters in string to lowercase
print(name.lower())

# Splits string according to delimiter and returns the list of substring. 
# Space is considered as the default delimiter.
print(name.split("a"))





#Creating a string
pancard_number="AABGT6715H"
#Length of the string
print("Length of the PAN card number:", len(pancard_number))
#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)
print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])

print("Iterating the string using keyword in")
for value in pancard_number:
    print(value)
print("Searching for a character in string")

#if "Z" in pancard_number:
#    print("Character present")
#else:
#    print("Character is not present")
#Slicing a string
#print("The numbers in the PAN card number:", pancard_number[5:9])
#print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])
#pancard_number[2]="A" #This line will result in an error, i.e., string is immutable
#print(pancard_number)