import re

# IdException is the base class and super class would be "Exception"
class IdException(Exception):
    pass

class Machine:
    def __init__(self, name, id):
        self._name = name
        self._id = id

        # Checking if any digit is available in ID using regular expression '\d' (checks for digit)
        # if not then raising "IdException" which we created above ^^
        if re.search(r"\d", self._id) is None:
            raise IdException("Machine ID contains no number")

    def __str__(self):
        return f'Name : {self._name}, ID : {self._id}'

    def get_name(self):
        return self._name
    
    def set_id(self, id):
        self._id = id

# "Machine" class is the super class for "Car" class
#  Now Car class can override methods from super class "Machine"
class Car(Machine):
    pass


def main():
    
    car1 = Car("Maruthi", "ABCD")
 

main()