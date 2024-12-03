import re

def main():
    text = """
        One
        Two
        Three
    """
    
    result = re.match(r"(.*One.*Two)$", text, re.DOTALL|re.MULTILINE)
    
    if result is None:
        print("No match")
    else:
        print(f"Match: '{result.group(1)}'")

main()