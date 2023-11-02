pizza_toppings =[]
prompt = "Please enter the pizza topping you would like added"
prompt += "\nEnter 'quit' if you would like to exit. "


while len(pizza_toppings) < 3:
    topping = input(prompt)

    if topping == "quit":
        break

    pizza_toppings.append(topping)
    print(f"Adding {topping.title()} to the pizza.\n")