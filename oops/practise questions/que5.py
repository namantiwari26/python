'''Design a program for creating a child class Teacher that inherits properties
from the parent class Staff.
'''
class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Teacher(Staff):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Call the parent class constructor
        self.subject = subject

    def display_info(self):
        super().display_info()  # Call the parent class method
        print("Subject:", self.subject)

# Example usage:
teacher = Teacher("John Doe", 35, "Mathematics")
teacher.display_info()
