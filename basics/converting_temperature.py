# Temp in Fahrenheit = (Temp in Celcius - 32) * 0.5556



# input functions always returns a string
temperature_f = input("Please enter temperature in Fahrenheit : " )

#temperature_f is a string object, we need to covnert that to float type to substract it from 32
temperature_c = (float(temperature_f) - 32) * 0.5556

print(temperature_c)

#temperature_c is a float type, need to convert that string as we are concating all strings in print(statement)
print(temperature_f + "Fahrenheit is equals to " + str(temperature_c) + "in Celcius")

