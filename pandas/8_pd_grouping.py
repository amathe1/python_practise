import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("/Users/Arunkumar_Mathe/Documents/python_practise/pandas/mall_customers.csv", index_col= 0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    # seeting max rows to display to a big value so that it will print all rows in data frame
    pd.set_option("display.max_rows", 200)
    
    # Group By Gender
    group = df.groupby(by="Gender")

    # It will print the type of group
    # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
    print(type(group))

    # To print number of groups
    print(group.ngroups)

    # To print all groups with index values
    # Key as name and values as indexes
    print(group.groups)

    # To print only keys
    print(group.groups.keys())

    # To print all rows with name as "Male"
    print(group.get_group('Male'))

    # To print all rows with name as "Male"
    print(group.get_group('Female'))

if __name__ == "__main__":
    main()