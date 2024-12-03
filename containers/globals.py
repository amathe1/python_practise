
# Declaring a global variable at the top of program
# Note the indentation
value = 2

# Points to note :
#     1. We can access a global variable inside a function
#     2. But if we want to re-assign the value of global variable then 
#        we should mention "global" keyword inside that function to tell that it is a global variable
#        Otherwise, we will see below error
#        UnboundLocalError: cannot access local variable 'value' where it is not associated with a value

def do_something():
    global value
    print(value)
    value = 4
    print(value)

def main():
    do_something()
    

main()