
def greet():
    print(1/0)

def do_greet():
    greet()

def main():
    try:
        do_greet()
    except:
        print("Something went wrong! ")

main()


"""
We can catch exceptiong in multi levels as above

- Exception occurs in greet()
- main() function not calling it directly
- main() called do_greet() which is calling greet() which is the place where we are expecting an exception

"""