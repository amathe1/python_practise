def do_greet():
    raise Exception("Raised an exception!")
    greet()

def greet():
    print("Hello Arun!")
    print(1/0)


def main():
    try:
        while True:
            print("Hello")
        do_greet()
    except KeyError as ke:
        print(f"Key Error occured : {ke}")
    except ZeroDivisionError as zde:
        print(f"Zero Division Error : {zde}")
    except Exception as e:
        print(f"Exception caught : {e}")
    except KeyboardInterrupt:
        print("Keyboard Interrupt exception caught : Program ended")

"""
KeyboardInterrupt is not a type of Exception().
Hence it won't caught with type Exception as shown above.

"""

main()