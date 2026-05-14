class Restaurant:
    '''This class represents a restaurant with a name and food type.'''
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    def rest_open(self):
        print(f"{self.rest_name} is open.")
    
    def add_num_served(self):
        served = int(input("How many customers served today? "))
        self.number_served += served
    
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")
    
    def customer_rating(self):
        try:
            rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? "))
            if rating < 1 or rating > 5:
                print("Please enter a number between 1 and 5.")
                return
            self.customer_ratings.append(rating)
            avg = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {avg:.1f}.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 5.")

# Three instances
restaurant1 = Restaurant('McDonalds', 'fast food')
restaurant2 = Restaurant('Nobu', 'Japanese cuisine')
restaurant3 = Restaurant('Olive Garden', 'Italian food')

# Test print_num_served and add_num_served
#restaurant1.print_num_served()
#restaurant1.add_num_served()
#restaurant1.add_num_served()
#restaurant1.print_num_served()

# Test customer_rating
#restaurant1.customer_rating()
#restaurant1.customer_rating()
#restaurant1.customer_rating()

#restaurant2.print_num_served()
#restaurant2.add_num_served()
#restaurant2.print_num_served()
#restaurant2.customer_rating()
#restaurant2.customer_rating()

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()
restaurant3.customer_rating()
restaurant3.customer_rating()