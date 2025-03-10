"""

This program is for understanding why we have to write main() method as ' if __name__ == "__main__" '

Points to remember :
1. As we are importing 'support_for_conditionally_running_main.py', 
   we just want the methods to be available, we don't want that program to run
2. If we don't use "if" condition in this program while calling main(), 
   this will actuall run the program "support_for_conditionally_running_main.py" as well which we don't want
3. In every python program, "__name__" is equal to "__main__", if you run same program from itself
4. Hence always use below method while calling main

Example :

if __name__ == "__main__":
    main()

This will run only this program, and if ther are any import statements then this program will make sure that 
only methods in those programs are available (instead of running that program)



"""



import support_for_conditionally_running_main as scr

def main():
    scr.print_name()

if __name__ == "__main__":
    main()