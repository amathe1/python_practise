

import pandas as pd
import numpy as np

def main():
    
    # Initiating a dictionary and assigning some values; (key, value) pairs
    data = {

        'one' : [1, 2, 3],
        'two' : [-10, 20, -5],
        'three': [0.1, 0.2, 0.3]
    }
    # Creating a data frame from above dict using DataFrame in Pandas
    df = pd.DataFrame(data)

    print(df)
    print()

    # Multiplying entire data frame with o.5
    df = df * 0.5
    print(df)

    print()

    # converting entire data frame into it's sin values using numpy
    df = np.sin(df)
    print(df)

    # changing entire middle column (column index : 0, 1, 2)
    # Ex : iloc[row start index : row end index, column index]
    df.iloc[:, 1] = 5
    print(df)

if __name__ == "__main__":
    main()



