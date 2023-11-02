rental_car = input("What rental car would you like? ")
print(f"Let me see if I can find you a {rental_car}.")

dinner_group_size = input("How many people are in your dinner party? ")
dinner_group_size = int(dinner_group_size)

if dinner_group_size > 8:
    print("You'll have to wait for a table.")
else:
    print("I've got a table available for you.")

number = input("Please provide me with a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")