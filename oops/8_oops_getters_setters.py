"""

Note : getters & setters don't have importance as they have in other object oriented programming languages

"""

class Machine:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def __str__(self):
        return f'Name : {self._name}, ID : {self._id}'

    def get_name(self):
        return self._name
    
    def set_id(self, id):
        self._id = id




def main():
    
    m = Machine("THX1138", 1234)
    print(m)
    #print(m.get_name())
    #m.set_id(5678)

main()