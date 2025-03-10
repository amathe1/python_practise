import numpy as np

data_set1 = np.array([10, 20, 30, 40, 50, 60], dtype=int)
print(data_set1)
print("Dimension before reshaping : ", data_set1.ndim)
print()

data_set2 = data_set1.reshape(3, 3)


'''
Output :

[10 20 30 40 50 60]
Dimension before reshaping :  1

Traceback (most recent call last):
  File "d:\GitHub\Python\python_practise\numpy\np_practise.py", line 8, in <module>
    data_set2 = data_set1.reshape(3, 3)
                ^^^^^^^^^^^^^^^^^^^^^^^
ValueError: cannot reshape array of size 6 into shape (3,3)

'''