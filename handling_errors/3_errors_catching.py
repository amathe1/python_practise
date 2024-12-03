def do_greet():
    d =dict()
    print(d["one"])
    greet()

def greet():
    print(1/0)

def main():
    try:
        do_greet()
    except KeyError:
        print("A key error occured")
    except ZeroDivisionError:
        print("Tried to divide by zero!")
    except:
        print("Some unknown error occured")

main()