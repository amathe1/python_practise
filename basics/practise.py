"""
Multiplying a string with '0' will result in a empty string`

"""

y = ("Python" * 0) + "is amazing!"
#print(y)


boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))
if(boarding_call.find("AL"))>=0:
    print("Welcome to Air Lines.")
if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")
a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")
print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
message="Thank you all..Have a nice journey!"
print(message.upper())
print(message.lower())


