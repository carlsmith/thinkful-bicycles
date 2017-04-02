import random
from bicycles import Bicycle, BikeShop, Customer

# First create a list of Bikes, then create a BikeShop, stocking it
# with the Bikes...

bikes = [
    Bicycle("Rock Hopper", 75, 100), Bicycle("Dirt Jumper", 70, 150),
    Bicycle("Speed Demon", 50, 250), Bicycle("Mountaineer", 90, 350),
    Bicycle("Road Master", 65, 100), Bicycle("Ghetto King", 75, 550)
    ]

shop = BikeShop("Surplus Cycles", 20, bikes)

# Now, create a list of Customers, then iterate over them, printing
# the Customer's name and the Bikes that they can afford...

customers = [Customer("Ali", 200), Customer("Bob", 500), Customer("Caz", 1000)]

for customer in customers:

    bikes = ", ".join( bike.model for bike in shop.filter(customer.fund) )
    print customer.name, "|", bikes

# Print the BikeShop before making any sales...

print shop

# Iterate over the customers, selling each a Bike, then using a template,
# print who the customer is, what they bought, what it cost, and how much
# they have left over...

template = "{0} bought the {1} at ${2}, and they have ${3} left over."

for customer in customers:
    
    affordables = shop.filter(customer.fund)
    shop.sell(random.choice(affordables), customer)
    
    print template.format(
        customer.name, customer.bike.model,
        customer.bike.price, customer.fund
        )

# Print the BikeShop again, now it's made a few sales...

print shop
