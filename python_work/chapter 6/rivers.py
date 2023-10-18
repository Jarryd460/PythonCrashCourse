rivers = {"nile": "egypt", "orange": "south africa", "salt": "south africa"}
for key, value in rivers.items():
    print(f"The {key.title()} river runs through {value.title()}.")

print()
for key in rivers.keys():
    print(key.title())

print()
for value in set(rivers.values()):
    print(value.title())

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

print()
people_who_should_take_poll = ["jen", "adam", "edward", "steven", "sarah", "phil"]

for name in people_who_should_take_poll:
    if name in favourite_languages:
        print(f"Thank you {name} for taking the poll.")
    else:
        print(f"{name}, I invite you to please take the poll.")