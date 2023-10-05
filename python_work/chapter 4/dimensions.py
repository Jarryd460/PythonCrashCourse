# Tuples are lists that cannot change in size or value
dimensions = (200, 5)
print(dimensions[0])
print(dimensions[1])

# Tuples are defined by the comma
my_t = (3,)

print("")
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
