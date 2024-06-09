'''Create a Python program to define a person class with attributes like name,
country, and date of birth, and implement a method for determining the
person’s age
'''
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year 
        return age

# Example usage:
person1 = Person("Alice", "USA", "2007-03-26")
person2 = Person("Bob", "Canada", "1985-10-20")

print("Age of", person1.name, ":", person1.calculate_age())
print("Age of", person2.name, ":", person2.calculate_age())
