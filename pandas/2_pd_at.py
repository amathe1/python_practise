"""

Let's look at getting and setting values in a pandas data frame

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
    print(df.iat[1, 0]) # index 1 i.e., Tuesday, index 0 ie., Pullups ==> value must be '11'

    print()
    print(df.at['Sun', 'Crunches'])
    
    print()
    #Updating values based on rown & column names
    df.at['Sun', 'Crunches'] = 80
    print(df.at['Sun', 'Crunches'])

if __name__ == "__main__":
    main()