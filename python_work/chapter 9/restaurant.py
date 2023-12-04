class Restaurant:
    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and focuses on {self.cuisine_type}. They have served {self.number_served} people.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served += 1
        