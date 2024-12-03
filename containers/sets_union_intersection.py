
def sets_union_intersection():
    numbers1 = {1, 2, 3, 4, 5,6, 10}
    numbers2 = {0, 3, 4, 5, 7, 8, 9, 10}

    # union() will print all elements in both the sets (excluding duplicates)
    print(numbers1.union(numbers2))
    print()

    # intersection() will print common elements in both the sets
    print(numbers1.intersection(numbers2))
    print()

    # difference() will print elements in set1 but not in set2
    print(numbers1.difference(numbers2))  # can also be written as print(numbers1 - numbers2)
    print()

    # will print elements in set2 but not in set1
    print(numbers2.difference(numbers1))
    print()

    # Similar to numbers1.difference(numbers2) + numbers2.difference(numbers1)
    print(numbers1.symmetric_difference(numbers2))
    print()

def main():
    sets_union_intersection()

main()