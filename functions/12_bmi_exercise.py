"""

write a function that asks the user to enter their weight in kilos
and height in meters, them calculates BMI.

(weight divided by height times height)

The function should return all three values.

"""

def calculate_bmi():
    weight = input("Enter your weight in kilos: ")
    height = input("Enter your height in meters: ")

    weight = float(weight)
    height = float(height)

    bmi = weight / (height * height)

    return weight, height, bmi

def main():
    weight, height, bmi = calculate_bmi()

    print("weight : ", weight)
    print("height : ", height)
    print("bmi    : ", bmi)

main()