import re

def main():
    
    """
    
    .   Wildcard
    \s  space
    \S  non-space
    \w  number, letter, underscore
    \d  digit
    \D  non-digit
    \n  newline
    \r\f    carriage return or form feed
    
    []  Character class, matches one of several characters
    ()  group
    (?: )   Not a group; used just for removing ambiguity 
    (?= )   zero-width positive lookahead assertion
    (?! )   zero-width negative lookahead assertion
    |       Alternatives


    re.I    Ignore case
    re.M    Multiline; make ^ and $ match start and end of lines, not strings
    re.DOTALL   Make match newlines
    search
    match
    fullmatch

    *   Match zero or more  of the proceeding; greedy
    *?  Match zero or more  of the proceeding; non-greedy
    +   Match one or more  of the proceeding; greedy
    +?  Match one or more  of the proceeding; non-greedy

    split
    sub
    findall


    
    
    """
    
    text = "apple orange banana"

    # match sub string from starting of given input string
    print(re.match("apple", text))

    # match sub string from anywhere from given input string
    print(re.search("orange", text))

     # only matches entire string
    print(re.fullmatch("apple orange banana", text))



main()