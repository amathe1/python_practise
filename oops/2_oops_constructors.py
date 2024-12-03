"""

__init__() is the constructor
It will call everytime when we create an object for that class
We can pass arguments into constrcutor as shown below

"""



class Person:

    # __init() is the constructor
    def __init__(self, name):
        print(f"Class object created for {name}")

    def eat(self):
        print("Iam eating .......")
    
    def talk(self):
        print("Iam talking.....")



def main():
    person1 = Person("Arun")
    person2 = Person("Thoshith")
    person3 = Person("Anupama")

    person1.eat()
    person2.talk()

main()