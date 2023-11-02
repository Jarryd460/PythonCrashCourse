responses = []
polling_active = True
prompt = "If you could visit one place in the world, where would you go? "

while polling_active:
    vacation_place = input(prompt)
    responses.append(vacation_place)

    continue_poll = input("Continue poll? (yes/no) ")

    if continue_poll == "no":
        polling_active = False

print("\n--- Poll Results ---")
for response in responses:
    print(response)