"""
1. Python don't allow 2 functions with same name
2. Some programming languages like Java allows it (consider parameters are different)


"""


def greet(name):
    print("Hello", name)

def create_greeting(name):
    return "Hi " + name + "!"

# Note that return statement just return the data but it won't print it
# we have to take care of printing it wherever needed

def main():
    name = "John"
    greet(name)

    greeting = create_greeting(name)
    print(greeting)

main()