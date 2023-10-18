person = {"first_name": "Jarryd", "last_name": "Deane", "age": 31, "city": "Cape Town"}
print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person.get('age')}")
print(f"City: {person.get('city')}")

print()
people_favourite_numbers = {
    "Abby": 23,
    "Jane": 10,
    "Henry": 99,
    "Steven": 1,
    "Ben": 420
}

for person_favourite_number_key, person_favourite_number_value  in people_favourite_numbers.items():
    print(f"{person_favourite_number_key}'s favourite number is: {person_favourite_number_value}")

keywords_and_definitions = {
    "if": "Allows one to specify if a value is true then do this",
    "ifelse": "Allows one to specify if a value is true then do this otherwise do that",
    "for": "Repeats code x number of times",
    "range": "Generates x amount of numbers in the range specified",
    "list": "Attempts to cast the value to a list"
}

print()
for keyword in keywords_and_definitions:
    print(f"{keyword}: {keywords_and_definitions[keyword]}")