"""
ID  Weight  Height
1   70      160
2   60      155
3   100     180
"""

import pandas as pd

# The read_clipboard() method of Pandas creates a DataFrame from data copied to the clipboard. 
# It reads text from the clipboard and passes it to read_csv(), which then returns a parsed DataFrame object.
# So, make sure to copy above data every time before you run this program
df = pd.read_clipboard(index_col=0)

print(df)
print()

height = df['Height']
print(height)
print()

# This will return a pandas series object
# <class 'pandas.core.series.Series'>
# Series is like dict, keys & values
print(type(height))
print()

# index is of below type
# <class 'pandas.core.indexes.base.Index'>
print(type(height.index))

# this will print actual values in index
# Index([1, 2, 3], dtype='int64', name='ID')
print(height.index)

# this is an iterable object, if we can cast this to list we can see actual values
# output : [1, 2, 3]
print(list(height.index))
print()

#  <class 'numpy.ndarray'> : Values can actually stored as numpy arrays
print(type(height.values))

# [160, 155, 180]
print(list(height.values))


"""
Take away message here :

- Data frames are composite columns and each column is actually a series object
- Each series object has an index and values
- values are numpy arrays 
- And we can also run functions on series as : height.mean()

"""

