import re

def main():
    
    text = "one, two  , three, four"

    result = re.split("\s*,\s*", text)

    print(result)
    # prints a list
    # ['one', 'two', 'three', 'four']

main()