import re

def expand_string(s):
    return ''.join(int(num) * char for num, char in re.findall(r'(\d+)(\D)', s))

# Example usage
input_string = "4a3b"
print(expand_string(input_string))  # Output: aaaa



