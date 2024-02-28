class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'restaurant name is {self.name}')
        print(f'it has delicious {self.cuisine_type}')

    def open_restaurant(self):
        print(f'restaurant {self.name} is open')

    def set_number_served(self):
        print(f'restaurant served {self.number_served} people')

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('steak house', 'steak')

print(restaurant.name, restaurant.cuisine_type, restaurant.number_served)
restaurant.number_served = 10
restaurant.set_number_served()
restaurant.increment_number_served(30)
restaurant.set_number_served()
