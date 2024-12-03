"""
\w : Matches alphanumeric characters
+  : Matches one or more, as many as possible
\s : Matches a space 
\d : Matches a digit

"""


import re

def main():
    text = "The Temperature is 37."
    text = "The price is 4000."

    result = re.match("\w+\s\w+\s\w+\s\d+\.", text)
    print("No match" if result is None else f"'{result.group()}'")

main()