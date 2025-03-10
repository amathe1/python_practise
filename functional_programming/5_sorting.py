


def main():

    # Using lambda with sorted()
    # we are passing a list of tuples
    # It will sort second element in each tuple because key is x[1]
    # It will print in ascending order as reverse=False
    list3 = [(1, 2), (4, 5), (1, 1), (4, 3), (2, 4)]
    result3 = sorted(list3, key=lambda x : x[1], reverse=False)
    print(list(result3))


if __name__ == "__main__":
    main()