'''Present a Python code example showcasing data overloading using multiple constructors with different parameters
'''
class MyClass:
    def __init__(self, *args):
        if len(args) == 0:
            self.value = 0
        elif len(args) == 1:
            self.value = args[0]
        else:
            self.value = sum(args)

obj1 = MyClass()
obj2 = MyClass(10)
obj3 = MyClass(10, 20, 30)

print(obj1.value)  # Output: 0
print(obj2.value)  # Output: 10
print(obj3.value)  # Output: 60
