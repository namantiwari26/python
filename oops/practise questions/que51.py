""". Imagine you are designing a software system for a zoo. One of the key
features is managing different types of animals. You decide to use abstract
classes and methods to represent these animals.

1. Create an abstract class called Animal with the following abstract methods:

• make_sound: This method should be implemented by subclasses to
make the specific sound of each animal.

• move: This method should be implemented by subclasses to define
how each animal moves.

2. Create two subclasses of Animal called Lion and Monkey.
• For the Lion class, implement the make_sound method to roar and
the move method to walk.

• For the Monkey class, implement the make_sound method to
chatter and the move method to climb.

3. Instantiate objects of both Lion and Monkey classes and demonstrate their
functionalities by calling their make_sound and move methods.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Roar!"
    
    def move(self):
        return "The lion walks majestically."

class Monkey(Animal):
    def make_sound(self):
        return "Chatter chatter!"
    
    def move(self):
        return "The monkey climbs from branch to branch."

# Instantiate objects
lion = Lion()
monkey = Monkey()

# Demonstrate functionalities
print("Lion says:", lion.make_sound())
print("Lion moves:", lion.move())

print("Monkey says:", monkey.make_sound())
print("Monkey moves:", monkey.move())
