"""
Hashing algorithms

"""

values = { 1, 2, 3, "Arun", (1,2)}

print(hash("Arun"))

print()

"""
Traceback (most recent call last):
  File "/Users/Arunkumar_Mathe/Documents/python_practise/containers/hashing.py", line 12, in <module>
    print(hash((1,2, [1,2])))
          ^^^^^^^^^^^^^^^^^^

* list is mutable, hence we can't hash on it
"""
print(hash((1,2, [1,2])))