"""Develop a program for creating a class named Students, initializing attributes
such as name, age, and grade during object instantiation."""
#mine
class student:
    def __init__(self,name,age,grade,):
        self.name=name
        self.age=age
        self.grade=grade

student1=student("arnav",18,"B")
student2=student("drake",24,"A")

print("student 1:",student1.name,student1.age,student1.grade)
print("student 2:",student2.name,student2.age,student2.grade)

#chatgpt
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Example usage:
student1 = Student("Alice", 18, "A")
student2 = Student("Bob", 17, "B")

# Accessing attributes
print("Student 1:", student1.name, student1.age, student1.grade)
print("Student 2:", student2.name, student2.age, student2.grade)

