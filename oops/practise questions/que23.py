'''Discuss the use of the except clause without an exception type in Python
'''
#answer
'''In Python, the except clause without an exception type is used as a catch-all 
for any exception that occurs in the corresponding try block. 
This means that it will catch and handle any exception regardless of its type. 
However, using the except clause without specifying the exception type is generally considered less precise,
 and it may make debugging more difficult as it obscures the specific exceptions being handled.
'''
try:
    # Code that may raise an exception
    result = 10 / 0
except:
    # Handle any exception
    print("An exception occurred")
