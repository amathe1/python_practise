"""

itertools is a Python module that provides a collection of fast, memory-efficient tools 
for creating and working with iterators. It is part of Python’s standard library and is 
especially useful for data engineering, functional programming, and working with large datasets efficiently.

Let's see Grouping and Aggregation iterators

"""

from itertools import groupby


def enlarge_strr(s):
    return "".join(f"{len(list(group))}{char}" for char, group in groupby(s) )
    

def main():
    strr = "aaaaabbbbcccdde"
    print(enlarge_strr(strr))
 
    
main()

    
