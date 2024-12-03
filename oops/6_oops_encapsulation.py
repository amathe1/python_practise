"""
Classes having few methods with double underscore '__init__() , __str__()', called magic methods
basically used by python system by some special way like 
  - __init__() is a constructor method
  - __str__() will convert object to a string


Generally, if a method or a variable is not intended to be accessed by outside of a class,
then I will try to remember by prefix it with a underscore like "_brand", "_mileage" in below example.
Only the public interface of the class like "introduce()" should access them.
THIS IS CALLED ENCAPSULATION.

"""


class Cars:

    def __init__(self, brand, mileage):
        self._brand = brand
        self._mileage = mileage
    
    # __str__() method will convert an object into a string
    def __str__(self):
        return f"I am a car from brand '{self._brand}' \t with a mileage of '{self._mileage}'"

    def introduce(self):
        print(f"{self._brand} car will give a mileage of {self._mileage} kms per ltr")


def main():
    car1 = Cars("Baleno", 21)
    car2 = Cars("Mahendra SUV", 10)

    print(car1)
    print(car2)


main()