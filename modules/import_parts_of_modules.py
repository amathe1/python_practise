"""
we are importing the class with name Arun from greetings.py

Note that greetings.py is having other code as well


"""

from greetings import Arun


def importing_parts_of_other_modules():
    Arun.name()
    
def main():
    importing_parts_of_other_modules()

if __name__ == "__main__":
    main()