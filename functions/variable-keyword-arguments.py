

def describe_city(**attributes):

    for property in attributes:
        print(property, ": ", attributes[property])
        
    print()



def main():
    describe_city(name="Hyderabad", weather="cool", state="Telangana")
    describe_city(population=10000000, is_rainy=False)

main()