
class Person:
    def __init__(self, name):
        self._name = name
        print(f"Hello {self._name}")
        print(id(self._name))
        print(id(name))


def main():
    person1 = Person("Arun")

    print(person1._name)

main()