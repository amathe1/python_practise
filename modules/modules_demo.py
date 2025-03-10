"""
importing other python file(greetings.py)  using 'import' statement and creating a shortcut 'grt' for it

"""

import greetings as grt


"""
calling below methods() which are defined in other program 'greetings.py'


"""
def main():
    grt.informal_greeting()
    grt.formal_greeting()

main()