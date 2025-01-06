

import pandas as pd


def main():
    df = pd.read_csv('/Users/Arunkumar_Mathe/Documents/python_practise/pandas/exercises.csv', sep='\s*,\s*' )
    print(df)
    print(df.columns)

    print(df.head(2))
    print(df.tail(2))

main()