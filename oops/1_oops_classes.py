
"""
Procedural programming (PP)         : functions calling functions
Object-oriented programming (OOP)   : classes and objects
Functional programming (FP)         : passing functions to functions


"""

# A simple class with name "Person" (class name should start with capital letter)
# with 2 methods eat(), talk() which describes the activities of a person
# If a function belongs to a class, then we call them as methods

class Person:
    def eat(self):
        print("I'm eating!")

    def talk(self):
        print("I'm talking!")



def main():
    # Creating an object and assigning a variable to that to use it later
    person1 = Person()
    person2 = Person()

    # Calling the methods() in class using the object reference of that class
    person1.eat()
    person2.talk()

main()



