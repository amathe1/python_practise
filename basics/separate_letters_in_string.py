
def separate_letters_with_numbers(input_str):
    # empty list 
    result = []
    # initializing a variable with value 1
    count = 1
    # For loop on each charecter in the string
    for char in input_str:
        # We need only alphabets, hence looping in only if charecter is alphabet
        if char.isalpha():
            # if it is alphabet, then addiing that into above list(result) with count 1
            # count will increment if this alphabet repeat
            result.append((char, count))
            count += 1
    # returning result, which is a list with multiple tuples in it
    # Example :   [('a', 1), ('b', 1), ('c', 1), ('X', 1), ('Y', 1), ('Z', 1)]   
    
    return result
 
# Example usage:
input_str = "abcXYZ123!@#"

# Calling separate_letters_with_numbers() and passing above string as input
# output will receive the list result[] which contains a list of multiple tuples 
output = separate_letters_with_numbers(input_str)
 
# Looping the list result[] & passing first value in tuple to "letter" & second value in tuple to "number"
for letter, number in output:
    print(f"{letter} -> {number}")

