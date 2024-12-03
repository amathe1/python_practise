class Cars:

    def __init__(self, brand, mileage):
        self._brand = brand
        self._mileage = mileage

    def introduce(self):
        print(f"{self._brand} car will give a mileage of {self._mileage} kms per ltr")


def main():
    car1 = Cars("Baleno", 21)
    car2 = Cars("Mahendra SUV", 10)

    car1.introduce()
    car2.introduce()

main()