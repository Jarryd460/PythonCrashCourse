class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self)->str:
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odemeter(self):
        """Print a statement showing the cars mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odemeter(self, mileage):
        """
        Set the odemeter to the given value.
        Reject the change if it attempts to rollback the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Fill cars gas tank")
        