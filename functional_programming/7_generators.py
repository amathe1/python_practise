def main():
   
   #  Note that these are not comprehensions, these are generators which we casted into a container type
   print(list(x for x in range(0,5)))
   print(set(x for x in range(0, 5) if x!= 1))
   print(tuple('*' if x == 0 else x for x in range(0, 5)))

   # We can include both above conditions in one generator
   # while creating a tuple, it won't include '1' as we excluded it using condition at end 'if x!= 1'
   # Then it will replace '0' as '*' in tuple due to conition at start '* if x == 0 else x'
   print(tuple('*' if x == 0 else x for x in range(0, 5) if x!= 1))

if __name__ == "__main__":
    main()