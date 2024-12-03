import re

def main():
    text = """
        one
        two
        three
    """

    # Unlike match(), serch() won't start searching from start of string
    result = re.search(r"two", text)

    if result is None:
        print("No match")
    else:
        print(f"Match found : '{result.group(0)}'")

    

main()