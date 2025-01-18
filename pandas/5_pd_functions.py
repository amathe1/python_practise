"""

Let's see another way of initialising data frame and also getattr() built in function


Dataframe :
=========
       cow  goat  sheep
grass    1     2      3
grain    3     4      5
hay      5     6      7

"""

import pandas as pd


def main():

    # initiate a data frame by suppying array of arrays
    # inner array contains data for rows of data frame
    df = pd.DataFrame([[1, 2, 3],[3, 4, 5],[5, 6, 7]],
                      columns=['cow', 'goat', 'sheep'],
                      index=['grass', 'grain', 'hay']
                      )
    
    print()
    print(df)
    print()

    # Trying to call all the below functions on above data frame
    # getattr() is a built in function, allows you to dynamically access an object’s attributes or methods by name.
    for func in ['min', 'max', 'std', 'var', 'mean', 'sum']:
        f = getattr(df, func)
        print(func.title())
        print(f(axis=0))
        print()

if __name__ == "__main__":
    main()