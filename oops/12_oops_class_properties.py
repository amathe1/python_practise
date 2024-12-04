
class Widget:

    # Note that below variable 'count' is class property
    # We need to use class name to actually change it i.e., Widget.count (BUT NOT like self.count)
    # we can still access this via "self" but it won't be useful as we can't change a class property using self
    count = 0

    def __init__(self, name):
        self._name = name
        Widget.count += 1
        print(f'{Widget.count} widgets created!')

    def __str__(self):
        return self._name


def main():
    widget1 = Widget("Project panel")
    widget2 = Widget("Terminal view")

    print(widget1)
    print(widget2)

    print(Widget.count)

main()