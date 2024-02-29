class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cant roll back odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        battery_range = 0
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225
        print(f'this car can go about {battery_range} miles on a full charge')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print(f'battery upgraded to {self.battery_size} kWh')


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print('\nBefore battery upgrade')
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
print("\nAfter battery upgrade:")
my_leaf.battery.get_range()