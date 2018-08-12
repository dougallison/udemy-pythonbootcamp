# Dictionary Access
#
# - The food variable will store a randomly chosen food string.
#   Some of these items are in the bakery_stock dictionary and
#   some are not.
# - Print out a string depending on if food is avalue in
#   bakery_stock. If food is contained in bakery_stock, print
#   out a string that states how many items are left:
#   '3 left' for example.
# - If food is not contained in bakery_stock, print out
#   'We don't make that.

# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche",
               "morning bun", "gummy bear", "tea cake"])

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if(bakery_stock.get(food)):
    print(f'{bakery_stock[food]} {food} left')
    #print('{} left'.format(bakery_stock[food]))
else:
    print(f'We don\'t make {food}')
