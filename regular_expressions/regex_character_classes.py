import re

def main():
    text = "john.purcell@caveofprogramming.com"
    # [a-z] only match first character, [a-z\-\.]+ matches one or more characters that contains '.', '-' and '+' will match max possible chracters
    # we made indexes here by mentioning, 3 brackets (0) (1) (2) 
    # later collected them using name name, domain, suffix using result.groups()
    result = re.match("([a-z\.\-]+)@(\w+)\.(\w+)", text)
    print("No match" if result is None else f"Match found : '{result.group()}'")
    name, domain, suffix = result.groups()
    print(name, domain, suffix)

main()