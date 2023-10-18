person_0 = {"first_name": "Jarryd", "last_name": "Deane", "age": 31, "city": "Cape Town"}
person_1 = {"first_name": "Miche", "last_name": "Nicholas", "age": 28, "city": "Cape Town"}
person_2 = {"first_name": "Adam", "last_name": "Donald", "age": 43, "city": "Durban"}

people = [person_0, person_1, person_2]

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()

print()
animal_0 = {"kind": "dog", "name": "duke", "color": "brown", "owner": "jarryd"}
animal_1 = {"kind": "dog", "name": "amber", "color": "brown", "owner": "miche"}
animal_2 = {"kind": "cat", "name": "amber", "color": "black/white", "owner": "adam"}

pets = [animal_0, animal_1, animal_2]

for pet in pets:
    print(f"Kind: {pet['kind'].title()}")
    print(f"Name: {pet['name'].title()}")
    print(f"Color: {pet['color'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print()

print()
favourite_places = {
    "jarryd": ["South Africa", "France", "Spain"],
    "miche": ["Egypt", "Poland"],
    "pete": ["Argintina", "New Zealand", "Chile"]
}

for name, favourite_place in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in favourite_place:
        print(f"\t{place.title()}")
    print()