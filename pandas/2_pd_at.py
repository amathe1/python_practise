"""

Let's look at getting and setting values in a pandas data frame

====== DATA FRAME ======
     Pullups  Pushups  Crunches
Day                            
Mon       10       10         5
Tue       11        9         5
Wed       10        6         8
Thu       14       11         5
Fri        8       11         3
Sat       20       10         9
Sun        6        7         8

"""


import pandas as pd


def main():
    df = pd.read_csv('/Users/Arunkumar_Mathe/Documents/python_practise/pandas/exercises.csv', sep='\s*,\s*', index_col=0)
    print(df)

    print()
    # printing value based on rown & column names
    print(df.at['Mon', 'Pullups'])

    print()
    # printing value based on rown & column values
    print(df.iat[1, 0]) # row index is 1 i.e., Tuesday; and column index 0 ie., Pullups ==> value must be '11'

    print()
    print(df.at['Sun', 'Crunches'])
    
    print()
    #Updating values based on rown & column names
    df.at['Sun', 'Crunches'] = 80
    print(df.at['Sun', 'Crunches'])
    print()
    print(df)

if __name__ == "__main__":
    main()