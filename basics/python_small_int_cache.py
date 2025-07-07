"""
Python employs a technique called small integer caching to optimize memory usage and improve performance. 
This caching mechanism pre-allocates and stores integer objects within a specific range, typically from -5 to 256.

When an integer within this range is created, instead of allocating new memory, Python reuses the existing cached object. 
This means that multiple variables assigned the same small integer value will actually point to the same object in memory.

"""

a = -5
b = -5

print(id(a))
print(id(b))