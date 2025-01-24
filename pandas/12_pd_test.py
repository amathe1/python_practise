import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("/Users/Arunkumar_Mathe/Documents/python_practise/pandas/mall_customers.csv", index_col= 0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    # We can filter data frame using column names 
    print(df.loc[(df['Gender'] == 'Female') & (df['Age'] == 32)])

"""
            Gender  Age  Income  Spending
CustomerID                               
70          Female   32      48        47
95          Female   32      60        42
144         Female   32      76        87
148         Female   32      77        74
182         Female   32      97        86
192         Female   32     103        69
"""
if __name__ == "__main__":
    main()