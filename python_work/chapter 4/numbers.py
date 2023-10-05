for value in range(1, 21):
    print(value)

print("")
# for value in range(1, 1_000_001):
#     print(value)

print("")
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("")
for value in range(1, 20, 2):
    print(value)

print("")
for value in range(3, 31, 3):
    print(value)

print("")
for value in range(1, 10):
    print(value ** 3)

print("")
cubes = [value ** 3 for value in range(1, 10)]
print(cubes)