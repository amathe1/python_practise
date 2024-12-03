"""
Please look at all built-in exceptions from python.org link as below :
https://docs.python.org/3/library/exceptions.html

"""


def do_greet():
    raise Exception("Raised an exception!")
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
    except Exception as e:
        print(f"Exception caught : {e}")
    


main()