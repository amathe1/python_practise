import re

def main():

    text = """
    1. Apple
    2. Mango
    3. Banana
    4. Grape
    5. Pineapple
    6. Lichi
    7. Starfruit
    8. Papaya
    9. Orange
    10. Avacado
    """
    
    # findall() return a list of fruits (without captured groups)
    result1 = re.findall(r"\d+\.\s\w+", text)
    print(result1)

    # findall() return a list of tuple (if we use capture groups)
    result2 = re.findall(r"(\d+)\.\s(\w+)", text)
    print(result2)

main()