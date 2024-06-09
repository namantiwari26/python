'''Explain how a destructor can be defined and utilized in a Python class.'''

#Answer
''' a destructor is a special method called __del__() 
that is automatically invoked when an object is about to be destroyed or deallocated.
 It is primarily used for releasing resources or performing cleanup actions before the object is removed from memory. 
 However, it's important to note that the timing of when the destructor is called is not guaranteed 
 due to Python's garbage collection mechanism
'''
class MyClass:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

obj = MyClass()
del obj  # Object destruction triggered explicitly
