
class Machine:

    count = 0

    def __init__(self):
        Machine.count += 1
        self._id = Machine.count

    def get_id(self):
        return self._id



def main():
    m1 = Machine()
    m2 = Machine()
    m3 = Machine()

    print(m1.get_id())
    print(m2.get_id())
    print(m3.get_id())

main()