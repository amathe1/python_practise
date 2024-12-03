import re

def main():
    text = "Oranges are nice!"

    regex = re.compile(r"O\w+s", flags=re.I)
    #print(regex)

    # Instead of compling a regular expression directly while using it
    # We can use compile() and cache it so that next time we use same regex, it won't compile again
    result = re.sub(regex, "Bananas", text)

    print(result)

main()