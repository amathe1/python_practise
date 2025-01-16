import numpy as np

def main():
    
    # arange : (start, end, stepsize)
    # default start value : 0
    # default stepsize : 1
    # we only mentioned end value, so start & stepsize will be default values
    # output : [0 1 2 3 4 5 6 7 8 9]
    num = np.arange(10)

    print(num)
    print()

    num = np.arange(10)
    
    # num = num * 2 ; each element will be multiplied with 2
    print(num * 2)
    print()
    
    # num = num + 2 : each element will be added with 2
    print(num + 2)
    print()

    # num = num ^ 2 (each item will be multiplied to itself)
    print(num ** 2)
    print()

    # sin of given value
    print(np.sin(num))

    # max of given value
    print(np.max(num))

    # mean of given value
    # mean : obtained by adding up all the numbers then dividing by the size of the data set
    # (0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)/ 10
    print("num is : ", num)
    print(np.mean(num))

    # standard deviation of given value
    print(np.std(num))

    # variance of given value
    print(np.var(num))
    

if __name__ == "__main__":
    main()