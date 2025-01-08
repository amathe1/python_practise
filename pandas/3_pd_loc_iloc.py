"""
Let's look at getting ranges of rows and columns

"""


import pandas as pd


def main():
    df = pd.read_csv('/Users/Arunkumar_Mathe/Documents/python_practise/pandas/exercises.csv', sep=',', index_col=0)
    df.columns = df.columns.str.strip()
    print(df)

    print()

    # Using names of rows(instead of index) 
    # notice that if you use named index, 'Fri' is also included (for int it will do n-1)
    print(df.loc['Mon':'Fri'])

    print()
    # we can also specify step size
    # Here step size is '2', hence every other row will print starting with 'Mon' & ending with 'Fri'
    print(df.loc['Mon':'Fri':2])

    print()
    # Row range starting with 'Thu' & ending with 'Fri'
    # Column range starting with 'Pullups' & ending with 'Pushups'
    print(df.loc['Thu':'Fri', 'Pullups':'Pushups'])

    print()
    # if we only want Pullups & Crunches then use advanced indexing using a list as below
    print(df.loc['Thu':'Fri',['Pullups', 'Crunches']])

    print()
    # if need from beginning of the row, then we can just leave start range as empty as below
    # start range is empty, so it will start from first row
    print(df.loc[:'Fri',['Pullups', 'Crunches']])

    print()
    # if we need entire table
    print(df.loc[:,:])

    print()
    # Using iloc
    # we need to include ranges(int values)
    # Row start range is empty, means it will start from range '0'
    # Row end range is '6', means 'Sun' but remember that range will end (n-1) for int ranges
    # Column start range is empty, means it will start from range '0'
    # Column end range is 2, means all 3 cloumns but as it is int type range, it will do (n-1)
    print(df.iloc[:6,:2])



if __name__ == "__main__":
    main()