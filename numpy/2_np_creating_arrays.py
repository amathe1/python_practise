
import numpy as np


def main():

    # zeros : create a numpy array that consists of zeros
    # dbtype : for builtin types like int, float quotes are not required, rest all needed a quote (ex : int64)
    print(np.zeros(5, dtype=int))
    print()

    # 2 rows and 3 cloumns
    values = np.zeros([2, 3])
    print(values)
    print()

    # Higher dimension arrays
    # 2 different arrays(2 slices) with size 3 * 3 (3 rows & 3 columns)
    # output : n dimensional array, how many dimension's(n) ?  3 
    values = np.zeros([2, 3, 3])
    print(values)
    print()
    print("n dimensional array, how many dimension's(n) ? ",values.ndim)
    print()

    # range
    # start with 2, end with 8 with a diff of 0.5 for each number
    # output : [2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5]
    print(np.arange(2, 8, 0.5))
    print()

    # linearly spaced
    # prints evenly spaces numbers in  between the numbers you specify (start, end also included)
    print(np.linspace(4, 8, 5))
    print()

    # random
    print(np.random.rand(10))
    print()

    # random, normally distributed
    print(np.random.randn(5))
    print()

    # reshape
    print(np.random.rand(9))
    # output : [0.78745444 0.80079909 0.43581451 0.89264545 0.65435662 0.36107204
    #           0.66655763 0.73187296 0.60180849]
    print()
    print(np.random.rand(9).reshape(3, 3))
    # Output :
    # [[0.83883639 0.11140244 0.64237916]
    # [0.89367736 0.03629831 0.93697926]
    # [0.37761257 0.44433329 0.92809054]]
    # "np.random.rand(9)" generated an 1 dimenstional array with 9 random values and "reshape(3, 3) converted it into 3 * 3 array"
    print()


if __name__ == "__main__":
    main()