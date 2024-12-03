def error_trace():
    print(1/0)

def main():
    error_trace()

main()


"""

Traceback (most recent call last):
  File "/Users/Arunkumar_Mathe/Documents/python_practise/handling_errors/errors_traceback.py", line 7, in <module>
    main()
  File "/Users/Arunkumar_Mathe/Documents/python_practise/handling_errors/errors_traceback.py", line 5, in main
    error_trace()
  File "/Users/Arunkumar_Mathe/Documents/python_practise/handling_errors/errors_traceback.py", line 2, in error_trace
    print(1/0)
          ~^~
ZeroDivisionError: division by zero



Stack Trace : Trace of what's happening on the stack
Computer programs in general manage an area of memory, called the "stack".
Memory structures are called stacks, add and remove items from the top.
Stack is is used to hold the values of local variables, also used to recovrd which functions calls which otherfunction.
Last In First Out :


|---------|
|---------|
|---------|
|---------|
|---------|         

"""