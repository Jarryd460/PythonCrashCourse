# Imports all functions in pizza.py
import pizza
# Imports just make_pizza function in pizza.py
from pizza import make_pizza
# Imports just make_pizza function in pizza.py and gives it an alias of build_pizza
from pizza import make_pizza as build_pizza
# You can modules an alias as well
    # import pizza as pz
# To avoid having to specify the module (pizza.make_pizza), you can import all functions
    # from pizza import *

make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
build_pizza(10, "cheese", "ham", "avocardo")