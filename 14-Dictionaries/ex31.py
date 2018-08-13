# Given a diction named `inventory`:
#   1 - Make a copy of `inventory` and save it to a variable called
#       `stock_list` using a dictionary method.
#   2 - Add the value 18 to `stock_list` under the key 'cookie'
#   3 - Remove cake from `stock_list` using a dictionary method

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list = inventory.copy()
print(stock_list)

stock_list.update({'cookie': 18})
print(stock_list)

stock_list.pop('cake')
print(stock_list)
