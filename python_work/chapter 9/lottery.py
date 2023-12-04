from random import choice

alphanumeric_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")

first_choice = choice(alphanumeric_values)
second_choice = choice(alphanumeric_values)
third_choice = choice(alphanumeric_values)
fourth_choice = choice(alphanumeric_values)

print("Any ticket that matches the below wins: ")
print(first_choice)
print(second_choice)
print(third_choice)
print(fourth_choice)

my_ticket = ("a", 4, 10, "e")
winner = False
iterations = 0

while winner == False:
    iterations += 1    
    winning_values = []
    winning_values.append(choice(alphanumeric_values))
    winning_values.append(choice(alphanumeric_values))
    winning_values.append(choice(alphanumeric_values))
    winning_values.append(choice(alphanumeric_values))

    for value in my_ticket:
        if value in winning_values:
            winner = True
            continue
        winner = False
        break
        

print(f"It took {iterations} to win!")