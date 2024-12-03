
def basic_understanding_of_this_concept(dictionary):
    for name, hobbies in dictionary.items():
        print(name)
        print("=====")
        for hobby in hobbies:
            print(hobby)
        print()


def main():

    dictionary = {
        "Arun" : ["Coding", "Travelling", "Movies"],
        "Anupama" : ["Fitness", "Binge", "Sleeping"]
    }
    
    basic_understanding_of_this_concept(dictionary)

    
    
main()