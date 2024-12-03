"""

"Animal" is the super class
"Cat" is the subclass of type Animal

"""

# Super class
class Animal:
    def speak(self):
        print("I am an Animal")
    
    def eat(self):
        print("I am eating")

# Sub class 'Cat' inheriting super class 'Animal'
class Cat(Animal):
    # Overriding method speak() from super class Animal
    # and then having it's own implementation in sub class
    def speak(self):
        print("Meowwwwwww!")

def main():
    cat1 = Cat()
    cat1.speak()
    cat1.eat()

main()