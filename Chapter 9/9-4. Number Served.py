class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'We have {self.restaurant_name} restaurant.')
        print(f'Its cuisine type is {self.cuisine_type}.')
        print(f'Number of customers the restaurant served is {self.number_served}.\n')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!\n')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, additional):
        self.number_served += additional


restaurant = Restaurant('Albaik', 'chicken')
restaurant.describe_restaurant()

restaurant.number_served = 600
restaurant.describe_restaurant()

restaurant.set_number_served(700)
restaurant.describe_restaurant()

restaurant.increment_number_served(100)
restaurant.describe_restaurant()
