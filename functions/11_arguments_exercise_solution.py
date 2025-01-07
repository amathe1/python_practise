"""
define a single function that accepts:
.....one or more positional arguments
.....zero or more variable arguments
.....zero or more varibale keyword arguments

Make the function print all arguments it receive.


"""

def final_function(length, width, *args, **kwargs):
    print(length)
    print(width)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, ": ", kwargs[key])


def main():
    final_function(10, 20)
    print()
    final_function(30, 40, "Arun", "Ashok")
    print()
    final_function(50, 60, height=170, weight=90, color="brown", sex="male")

main()