from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavours: []):
        super().__init__(name, cuisine_type)
        self.flavours = flavours

    def ice_cream_flavours(self):
        print("We off the below ice cream flavours: ")
        for flavour in self.flavours:
            print(flavour.title())

print()
my_ice_cream_stand = IceCreamStand("Ice cream man", "desert", ["chocolate", "vanilla", "strawberry", "plain"])
my_ice_cream_stand.ice_cream_flavours()