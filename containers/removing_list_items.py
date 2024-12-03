
def removing_list_items():
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

    # remove elements using slicing
    days[0:3] = []
    print(days)

    # removing using remove(method)
    days.remove("Sat")
    print(days)
    
    #removing elements using pop() method, it will remove first element
    days.pop(0)
    print(days)

    # removing elements using del option
    del days[1]
    print(days)

    del days
    #print(days)


def main():
    removing_list_items()

main()