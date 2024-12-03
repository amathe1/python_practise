"""
    We can format string using place holders as below.
""" 

def main():
    # '%s' is the place holder of type STRING
    # ("Arun!", "Friday")  is a TUPLE
    print("Hello %s, today is %s." % ("Arun!", "Friday"))  

    # '%d' is the place holder of type decimal(int)
    print("Hello %s. You are having %d years of experince at Infosys Ltd." % ("Arun", 9))

    # '%f' is the place holder of type FLOAT
    print("Temperature today is %f." %35.12345)
    # '.2' will print only 2 values after '.'
    print("Temperature today is %.2f." %35.12345)
    # adding '10' before .2f will give a 10 characters space between string and the place holder
    print("Temperature today is %10.2f." %35.12345)

main()