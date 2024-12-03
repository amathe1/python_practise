"""
Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false. Invoke the function and based on return value print the numbers are amicable numbers or not.

num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of num1 is equal to num2 and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.

Example: 220 and 284 are amicable numbers as

Proper devisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284

Proper devisors of 284 are 1, 2, 4, 71, 142 whose sum is 220

"""
import math

def divided_sum_val(my_val) :

   res = 0
   print("=================> " , int(math.sqrt(my_val))+1)
   for i in range(2, int(math.sqrt(my_val)) + 1) :

      if (my_val % i == 0) :

         if (i == int(my_val / i)) :
            res = res + i
         else :
            res = res + (i + int(my_val / i))
   return (res + 1)

def check_amicable(x, y) :

   if (divided_sum_val(x) != y) :
      return False

   return (divided_sum_val(y) == x)

first_num = 220
second_num = 288
print("The numbers are :")
print(first_num)
print(second_num)
if (check_amicable(first_num, second_num)) :
   print ("The given numbers are amicable in nature")
else :
   print ("The given numbers are not amicable in nature")