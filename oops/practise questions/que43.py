''' Design a system to model vehicles. Start with a base class Vehicle with 
attributes like make, model, and year. Derive subclasses like Car, Truck, and 
Motorcycle. How would you handle specific methods or attributes for each 
subclass, such as cargo_capacity for trucks and seating_capacity for cars? 
'''

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, seating_capacity):
        super().__init__(make, model, year)
        self.seating_capacity = seating_capacity

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

# Example usage
car = Car("Toyota", "Camry", 2022, 5)
print("Car:", car.make, car.model, car.year, "Seating Capacity:", car.seating_capacity)

truck = Truck("Ford", "F-150", 2020, "1000 lbs")
print("Truck:", truck.make, truck.model, truck.year, "Cargo Capacity:", truck.cargo_capacity)

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
print("Motorcycle:", motorcycle.make, motorcycle.model, motorcycle.year)
