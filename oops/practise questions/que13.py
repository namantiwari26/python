'''Demonstrate method overriding in Python to achieve runtime polymorphism with a code example.
'''

#Answer
'''
Method overriding occurs when a subclass provides a specific implementation of a method that is already defined 
in its superclass. This allows the subclass to customize or extend the behavior of the method while maintaining 
the same method signature.
'''
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

# Example usage:
 # Output: Animal makes a sound

dog = Dog()
dog.sound()  # Output: Dog barks
