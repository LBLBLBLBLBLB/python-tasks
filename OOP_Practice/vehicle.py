class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers'


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


bus1 = Bus('mercedes', 20, 30)
print(bus1.seating_capacity())
car1 = Vehicle('bmw', 10, 30)
print(car1.seating_capacity(20))

print(bus1.name, bus1.max_speed, bus1.mileage)
print(car1.name, car1.max_speed, car1.mileage)
