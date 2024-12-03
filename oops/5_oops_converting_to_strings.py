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