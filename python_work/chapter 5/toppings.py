requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

requested_toppings = ["mushrooms", "pineapple", "onions"]

if "pineapple" in requested_toppings:
    print("pineapple has been included in the requested toppings!")

print()
requested_toppings =[]
# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

if requested_toppings:
    for topping in requested_toppings:
        if topping == "green peppers":
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")

print()
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished against pizza!")