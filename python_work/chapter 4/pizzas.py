pizzas = ["District 6", "Gimba", "Plain and Simple"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("")
print("Pizzas are so simple and tasty.")
print("I enjoy ones with Avo and Bacon.")
print("I like thin bases.")
print("I really love pizza")

friends_pizzas = pizzas[:]

pizzas.append("Mediterian")
friends_pizzas.append("Puffy")

print("")
print("My favourite pizzas are:")
for value in pizzas:
    print(value)

print("")
print("My friend's favourite pizzas are:")
for value in friends_pizzas:
    print(value)