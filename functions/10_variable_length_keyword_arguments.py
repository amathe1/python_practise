

def describe_city(**kwargs):

    for property in kwargs:
        print(property, ": ", kwargs[property])
        
    print()



def main():
    describe_city(name="Hyderabad", weather="cool", state="Telangana")
    describe_city(population=10000000, is_rainy=False)

main()


