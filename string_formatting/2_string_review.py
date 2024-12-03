"""

- concatination
- print multiple arguments
- string methods : lower, upper, casefold, join
- print termination character
- control characters / escape sequences \n \t \\

"""

def main():
    print("Hello " + "Arun!")
    print(10 + 21.22)
    print("Integer is seven " + str(7))
    print("Arun", 10, 21,121212, {1, 2, 3}, 'A')

    print("Hello".upper())
    print("HELLO".lower())
    print(" : ".join({"One", "Two", "Three"}))
    print("Hello :", end=".......")
    print("Arun!")

    print("Hi, Arun. \nHow are you doing ????")
    print("Hello Arun. \tHow are you ? \tHow is your day?")
    print("D:\\Documents\\Arun\\personal\\")

    print('"Hello"')
    print("'Hello'")

main()