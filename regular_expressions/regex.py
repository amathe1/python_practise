# importing regular expression module
import re

def main():
    text = "dog"

    # Using match() method in regular expression module
    # match(regular expression, text that you want to compare with)
    # d.g can match and string that start with 'd' and end with 'g'
    result = re.match("d.g", text)
    print(result is not None)


    text2 = "snoop"
    print(re.match("s...p", text2) is not None)
    

main()