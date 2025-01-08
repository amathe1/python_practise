"""
Variable/Arbitary arguments : 
when user don't know exactly how many arguments can enter, this is to handle such situation.

- name is an argument (positional arguments - has to be come first in arguments section of a method)
- attributes is also an argument
- *attributes is a variable length argument

"""



def describe_person(name, *args):
    print(name)
    # print(type(attributes))

    for arg in args:
        print(arg)



def main():
    describe_person("Pawan Kalyan", "Genuine", "Leader Material", "Honest")
    print()
    describe_person("CBN", "Visionary", "Growth Oriented")
    print()
    describe_person("Jagan")
   

main()