prompt = "what is your age (Enter '-1' to quit)? "

while True:
    age = input(prompt)

    age = int(age)

    if age == -1:
        break
    elif age <= 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(f"Your movie ticket price will be {price}\n")