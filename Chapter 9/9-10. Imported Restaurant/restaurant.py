class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'We have {self.restaurant_name} restaurant.')
        print(f'Its cuisine type is {self.cuisine_type}.\n')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!\n')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print('Ice cream flavors:')
        for flavor in self.flavors:
            print(f'- {flavor}')
