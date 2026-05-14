class Restaurant:
    '''This class represents a restaurant with a name and food type.'''
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Three instances
restaurant1 = Restaurant('McDonalds', 'fast food')
restaurant2 = Restaurant('Nobu', 'Japanese cuisine')
restaurant3 = Restaurant('Olive Garden', 'Italian food')

# Call both methods for each instance
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()