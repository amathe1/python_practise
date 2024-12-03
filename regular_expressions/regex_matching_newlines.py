import re

def main():
    text = """
        One
        Two
        Three
    """
    # .* won't be sufficient in this case because text is in multiline
    # and match() can't match '\n' & empty spaces until it reach first word in next line ....One
    # Hence we need to use re.DOTALL option inside match() to make '.*' match '\n' & empty spaces as well
    print(re.match(r".*Three", text, re.DOTALL))

    
    pass

main()