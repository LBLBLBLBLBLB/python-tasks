class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'restaurant name is {self.name}')
        print(f'it has delicious {self.cuisine_type}')

    def open_restaurant(self):
        print(f'restaurant {self.name} is open')


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print('flavors:')
        for flavor in self.flavors:
            print(f'\t {flavor}')


restaurant = Restaurant('steak house', 'steak')
ice_cream_stand = IceCreamStand('ice_cream', 'ice_cream', ['vanilla', 'chocolate'])
ice_cream_stand.display_flavors()
