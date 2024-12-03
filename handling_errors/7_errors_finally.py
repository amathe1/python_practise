"""
Please note that even an error occured or not, finally block will definately executed.
It is helpful to do some final operations like closing files which were opened as part of try block.

"""
def main():
    try:   #use raise to raise an exception intentionally
        raise ZeroDivisionError("Division by zero")
        raise KeyError("Key Error")
    except (ZeroDivisionError, KeyError) as e :
        print(f"Error occured : {e}")
    finally:
        print("Finally was executed")

main()