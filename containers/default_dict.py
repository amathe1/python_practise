from collections import defaultdict

def main():
    people = defaultdict(int)

    people.update({ "Arun" : "34", "Anupama" : 33, "Wine" : 1})

    print(people["Arun"])
    print()

    # when we try to get the value of a key which is not in dict, it will through "KeyError"
    # To fix this issue, we imported "defaultdict" from collections 
    # where we can pass the type of values, int in this case which has default value "0"
    # So, if we try to get the value of a key which is not in dict, 
    # then it will through the default value of type int "0"(instead of error)
    print(people["Ashok"])

main()