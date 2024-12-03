"""
Get the user to enter a temperature in celcius

temp < 0 : Print "Fridge too cold"
0 - 4    : Print "Fridge OK"
4 - 6    : Print "Fridge too warm"
  > 6    : Print "Fridge broken!"

"""

temp_c = input("Please enter the temperature in celcius : ")

temp = int(temp_c)

COLD = "Fridge too cold"
OK   = "Fridge OK"
WARM = "Fridge too warm"
BROKEN = "Fridge broken"

if (temp <= 0):
    print(COLD)
elif(temp <= 4):
    print(OK)
elif(temp <= 6):
    print(WARM)
else:
    print(BROKEN)