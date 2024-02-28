class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'restaurant name is {self.name}')
        print(f'it has delicious {self.cuisine_type}')

    def open_restaurant(self):
        print(f'restaurant {self.name} is open')


restaurant = Restaurant('steak house', 'steak')

print(restaurant.name)
print(restaurant.cuisine_type)
print()
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()
