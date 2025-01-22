import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("/Users/Arunkumar_Mathe/Documents/python_practise/pandas/mall_customers.csv", index_col= 0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    # seeting max rows to display to a big value so that it will print all rows in data frame
    pd.set_option("display.max_rows", 200)
    
    # Group By Gender
    group = df.groupby(by="Gender")

    print(type(group))
    # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

    male_dataframe = group.get_group('Male')
    print(type(male_dataframe))
    # <class 'pandas.core.frame.DataFrame'>
    
    male_income_series = male_dataframe['Income']
    print(type(male_income_series))
    # <class 'pandas.core.series.Series'>
    
    grouped_income_series = group['Income']
    print(type(grouped_income_series))
    # <class 'pandas.core.groupby.generic.SeriesGroupBy'>

  

if __name__ == "__main__":
    main()