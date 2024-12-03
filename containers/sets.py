numbers = {1, 2, 3, 4, 1, 2, 3, 4}
print(numbers)
print(type(numbers))

numbers_list = [1, 3, 5, 2, 5]
print(set(numbers_list))

print(2 in numbers_list)
print("2" in numbers_list)

"""
tuple : ordered, immutable, "in" is slow
list  : ordered, mutable, "in" is slow
set   : not ordered, mutable, "in" is fast
dict  : ordered, mutable

"""