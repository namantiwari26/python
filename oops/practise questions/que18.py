'''Define data overriding and provide an example demonstrating it in Python. 
'''

#Answer
'''Data overriding, also known as attribute overriding, occurs in inheritance when a subclass provides a specific
 implementation of an attribute that is already defined in its superclass. This allows the subclass to customize or
   extend the behavior of the attribute while maintaining the same name.
'''
class Parent:
    value = 10

class Child(Parent):
    value = 20  # Override 'value' attribute in Parent class

obj = Child()
print(obj.value)  # Output: 20
