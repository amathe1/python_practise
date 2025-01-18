
import pandas as pd

def main():
    # need to set CustomerID as index
    df = pd.read_csv("/Users/Arunkumar_Mathe/Documents/python_practise/pandas/mall_customers.csv", index_col= 0)
    
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    # set only first 10 rows 
    pd.set_option("display.max_rows", 10)

    # To sort values in data frame
    df.sort_values(by=['Gender', 'Age'],  inplace=True, axis=0, ascending=False)

    print(df)

if __name__ == "__main__":  
    main()