'''Explain the purpose of the raise statement in Python
'''

#answer
'''The raise statement is used to explicitly raise an exception in Python. 
It allows programmers to create custom exceptions or to re-raise exceptions caught in except blocks.
 This can be useful for signaling errors or exceptional conditions in code.
'''
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

try:
    validate_age(-10)
except ValueError as e:
    print(e)
