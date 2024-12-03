
def describe_person(name, *attributes):
    print(name)
   # print(type(attributes))


    for attribute in attributes:
        print(attribute)



def main():
    describe_person("Pawan Kalyan", "Genuine", "Leader Material", "Honest")
    print()
    describe_person("CBN", "Visionary")
    print()
    describe_person("Jagan")

main()