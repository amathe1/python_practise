
def sets_removing_items():
    #Creating a set 
    numbers1 = {x for x in range(20)}
    print(numbers1)
    print()

    #removing an item from set
    numbers1.remove(19)
    print(numbers1)
    print()

    # Use dicard instead of remove, discard will not error out even the element you are are trying to remove doesn't exist in set
    numbers1.discard(30)
    print(numbers1)
    print()

def main():
    sets_removing_items()

main()