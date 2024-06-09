'''Describe how to handle exceptions using try, except, and finally blocks in Python
'''
#answer
'''In Python, exceptions can be handled using the try, except, and finally blocks.
 The try block is used to enclose the code that may raise an exception,
   and the except block is used to handle the exception if it occurs. 
   The finally block is optional and is used to execute cleanup code regardless of whether an exception occurred.
'''
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the ZeroDivisionError exception
    print("Cannot divide by zero")
finally:
    # Cleanup code
    print("Finally block executed")
