"""
\w : Matches alphanumeric characters
+  : Matches one or more, as many as possible
\s : Matches a space 
\d : Matches a digit

"""


import re

def main():
    text = "The Temperature is: 37"
    # Note that we have kept '\d' inside brackets ( )
    # thus we can catch only that digit inside group() but with index '1'
    # if you use index as '0' then we still get whole string " 'The Temperature is: 37' "
    result = re.match(".*:\s(\d+)", text)
    print("No match" if result is None else f"'{result.group(1)}'")

main()