import calendar

def main():
    year = input("Enter year : ")
    year = int(year)
    is_leap = calendar.isleap(year)

    if is_leap :
        print(f"{year} is a leap year !")
    else:
        print(f"{year} is not a leap year !")

main()