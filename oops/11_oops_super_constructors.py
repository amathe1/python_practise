
# Super class
class Machine:
    # Constrcutor in super class
    def __init__(self, id, name):
        self._id = id
        self._name = name

# Sub class "Car" extending super class Machine
class Car(Machine):
    # Constructor in sub class
    def __init__(self, id, name, type):
        super().__init__(id, name)
        self._type = type

    def __str__(self):
        return f'ID {self._id} : Name {self._name} : Type {self._type}'

def main():
    # Created the object 'car1' for class Car
    # It will call the constructor '__init__' from class Car
    # But __init__ constructor in class Car doesn't have implementation for variables ID, Name
    # Hence using 'super()' method to call the constructor in super class 'Machine' to implement variables ID, Name
    car1 = Car("1234", "Maruthi", "Nexa")
    print(car1)

main()