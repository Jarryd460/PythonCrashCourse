my_foods = ["Pizza", "Falafel", "Carrot Cake"]
# Setting friends_foods to my_foods does not creat a separate list but rather a reference to the same list
# friend_foods = my_foods
friend_foods = my_foods[:]

my_foods.append("Cannoli")
friend_foods.append("Ice cream")

print("My favourite foods are:")
print(my_foods)

print("\nMy friends favourite foods are:")
print(friend_foods)

print("")
for value in my_foods:
    print(value)

print("")
for value in friend_foods:
    print(value)