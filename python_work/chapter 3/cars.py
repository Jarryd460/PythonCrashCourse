cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)

print("Length of list: " + str(len(cars)))

cars.sort(reverse=True)
print(cars)

# Displays the list in a sorted order but does not change the original list
print(sorted(cars))
print(cars)