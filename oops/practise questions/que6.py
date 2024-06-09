'''Devise a Python program to define a Vehicle class with instance attributes
max_speed and mileage.
'''
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Example usage:
car = Vehicle(200, 30)
print("Car Details:")
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)
