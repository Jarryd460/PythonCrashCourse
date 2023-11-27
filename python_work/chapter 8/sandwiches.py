def build_sandwich(*ingredients):
    print("\nThe ingredients for the sandwich you ordered is as follows: \n")

    for ingredient in ingredients:
        print(ingredient.title())

build_sandwich("ham", "cheese")
build_sandwich("chicken", "mayo", "lettus", "cucumber")
build_sandwich("peanut butter")

def make_car(manufacturer, model_name, **details):
    details["manufacturer"] = manufacturer
    details["model_name"] = model_name
    return details

my_car = make_car("Renault", "Clio", colour="white", year=2016)
print()
print(my_car)