def greeting(name):
    print("ID inside greeting method : " , id(name))
    
    name = "Bidhu"
    print("Hello " + name)
   # print("ID inside greeting method after modyfying value : " , id(name))


def main():
    #string objects in python are immutable
    name = "Arun"
 
    print("ID inside main method : " , id(name))
    greeting(name)


main()