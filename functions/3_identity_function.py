def greeting(name):
    print("ID inside greeting method : " , id(name))
    print("Hello " + name)


def main():
    #string objects in python are immutable
    name = "Arun"
 
    print("ID inside main method : " , id(name))
    greeting(name)

main()