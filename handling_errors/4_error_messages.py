"""

Associating messages with your exceptions

- An exceptions is also a kind of object like a string, int etc.,

"""


def do_greet():
    d = dict()
    print(d["hello"])
    greet()

def greet():
    print("Hello Arun!")
    print(1/0)


def main():
    try:
        do_greet()
    except KeyError as ke:
        print(f"Key Error occured : {ke}")
    except ZeroDivisionError as zde:
        print(f"Zero Division Error : {zde}")
    except:
        print("Some UNKNOWN error occured")


main()
