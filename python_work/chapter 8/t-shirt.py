def make_shirt(size, message):
    print(f"A {size} t-shirt will be sown with the message '{message}'.")

make_shirt("medium", "Hello World!")
make_shirt(message="YOLO", size="small")

def make_shirt_with_defaults(size="large", message="I love Python"):
    print(f"A {size} t-shirt will be sown with the message '{message}'.")

print()
make_shirt_with_defaults()
make_shirt_with_defaults("medium")
make_shirt_with_defaults("small", "It's been a while since I coded.")

def describe_city(city, country="South Africa"):
    print(f"{city} is in {country}.")

print()
describe_city("Cape Town")
describe_city("Johannesburg")
describe_city("Paris")