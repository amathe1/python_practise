"""

Numpy is a package that allows us to manipulate arrays of data.
Usually nymerical but we can also put strings in it.

We can easily manipulate numbers mathematically in a array.

It is like a array class but kind of tubo charged array (more power!)

Note : Please use 'pip3 list' and see if numpy is already installed in your machine.
       If not then, use 'pip3 install numpy' to install this python package


"""

import numpy as np



def main():
    # creating a one dimentional array/list using 'np'
    num1 = np.array([1, 2, 3, 4], dtype=int)

    print(num1)
    print()

    # How to check the type of array ?
    print("Type of the array is : ",num1.dtype)
    print()

    # How to check dimension of an array ?
    print("Dimension of the array is : ",num1.ndim)
    print()

    # What is the shape of the array ?
    print("Shape of the array is : ",num1.shape)
    print()

    # How many bytes does this array have ?
    print("Bytes : ", num1.nbytes)
    print()

    # # creating a two dimentional array/list using 'np'
    num2 = np.array([[1, 2], [3, 4], [5, 6]], dtype=int)

    print(num2)
    print()

    print(num2.dtype)
    print()

    print(num2.ndim)
    print()

    print(num2.shape)
    print()


if __name__ == "__main__":
    main()