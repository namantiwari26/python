''' Create a Python code example illustrating data overloading by defining 
multiple attributes with the same name in a class. 
'''
class MyClass:
    def __init__(self, value1, value2):
        self.value = value1
        self.value = value2  # Overloading 'value' attribute

obj = MyClass(10, 20)
print(obj.value)  # Output: 20


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x = x * 2
    def display(self):
     print(f"x: {self.x}, y: {self.y}")
p = Point(3,4)
p.display()


