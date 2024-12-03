import re

def main():
    text = "zigzag"
    # '.*' means match zero or more of any character
    result = re.match(".*", text)
    # combined ternary operator with 'f' prefix
    print("No match" if result is None else f"Match found : {result.group()}")

    # '*' operator if greedy, it match as much as possible
    result = re.match("z.*g", text)
    # combined ternary operator with 'f' prefix
    print("No match" if result is None else f"Match found : {result.group()}")

    # '?' before * makes it non greedy, meaning it will match as less as possible
    result = re.match("z.*?g", text)
    # combined ternary operator with 'f' prefix
    print("No match" if result is None else f"Match found : {result.group()}")

    # z.* will match whole string in text as .* is greedy
    # but having '?' after '.*' makes it non greedy though it has .* in regex
    # Hence minmal match would be some string starting with 'z' followed by nothing
    # (because '?' made it non-greedy to match minimal string)
    result = re.match("z.*?", text)
    # combined ternary operator with 'f' prefix
    print("No match" if result is None else f"Match found : {result.group()}")

    # '$' will match end of string, it is not matching a character
    # for regex "z.*?$" to match, end of the string must come after 'z.*?'
    # so, it will match complete string
    result = re.match("z.*?$", text)
    # combined ternary operator with 'f' prefix
    print("No match" if result is None else f"Match found : {result.group()}")




main()