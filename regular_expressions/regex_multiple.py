"""
Matching multiple characters

"""


import re


def main():
    text = "drooooool"

    # "dr.*" will match first 2 characters as dr and then .* means any character with any lenght
    result = re.match("dr.*", text)
    print(result.group())

main()
