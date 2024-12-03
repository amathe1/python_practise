

def main():
    months = { "Jan" : "January", "Feb" : "February", "Mar" : "March" }
    #print(months)

    months["Apr"] = "April"
    #print(months)

    # Using update() method to add additinal elements in below dictionary "months"
    months.update({"May" : "May", "Jun" : "June"})
    print(months)


main()