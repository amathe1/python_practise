import re

def main():
    text = "Hello Arun, Hello Anu, Hello Vynateya"

    result = re.sub(r"Hello (Arun|Anu|Vynateya)", r"Hi \1", text)

    print(result)

main()