from car import Car
from electric_car import ElectricCar

my_new_car = Car("Audi", "A4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odemeter()
my_new_car.odometer_reading = 23
my_new_car.read_odemeter()
my_new_car.update_odemeter(100)
my_new_car.read_odemeter()
my_new_car.update_odemeter(0)

print()
my_used_car = Car("suburu", "outback", 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odemeter(23_500)
my_used_car.read_odemeter()
my_used_car.increment_odometer(100)
my_used_car.read_odemeter()

print()
my_car = ElectricCar("Nissan", "leaf", 2024)
print(my_car.get_descriptive_name())