from restaurant import Restaurant

my_restaurant = Restaurant("Wajids", "Pakistani cuisine")
print(f"Restaurant name: {my_restaurant.restaurant_name}")
print(f"Restaurant cuisine type: {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant_1 = Restaurant("KFC", "American")
restaurant_1.number_served = 10
Restaurant_2 = Restaurant("All the way to India", "Indian cuisine")
Restaurant_2.set_number_served(5)
restaurant_3 = Restaurant("Pasta me", "Italian cuisine")
restaurant_3.increment_number_served()
restaurant_3.increment_number_served()

print()
restaurant_1.describe_restaurant()
Restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
