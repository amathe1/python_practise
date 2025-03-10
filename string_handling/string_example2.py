"""

For a given input string like : 4a3b2c, we should print "aaaabbbcc"

Points to remember :
1. We can use Python regular expressions to match the pattern


"""


import re

def expand_string(s):
    return ''.join(int(num) * char for num, char in re.findall(r'(\d+)(\D)', s))

# Example usage
input_string = "4a3b2c"
print(expand_string(input_string))  # Output: aaaa




