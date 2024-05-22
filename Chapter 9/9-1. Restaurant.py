class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'We have {self.restaurant_name} restaurant.')
        print(f'Its cuisine type is {self.cuisine_type}.\n')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!\n')


restaurant = Restaurant('Albaik', 'chicken')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
restaurant = Restaurant('Alromansia', 'rice')
restaurant.describe_restaurant()
restaurant = Restaurant('Abo alaiz', 'fast food')
restaurant.describe_restaurant()
restaurant = Restaurant('Humbergino', 'burger')
restaurant.describe_restaurant()



