sandwich_orders = ["district 6", "pastrami", "mount nelson", "pastrami", "plain and simple", "heart attack", "pastrami"]
finished_sandwiches = []

print("The Deli has run out of pastrami sandwich")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)