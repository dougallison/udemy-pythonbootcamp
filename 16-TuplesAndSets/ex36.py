# 1 - Create a variable called numbers which is a tuple with the
#     values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)
print(numbers)

# 2 - Create a variable called value which is a tuple with the
#     value 1 inside
value = (1,)
print(value)

# 3 - Given the `values` variable, create a variable called
#     static_values which is the result of the values
#     variable converted to a tuple.
values = [10, 20, 30]
static_values = tuple(values)
print(static_values)

# 4 - Given the `stuff` variable, create a variable called
#     `unique_stuff` which is a set of only the unique values
#     in the stuff list.
stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]
unique_stuff = set(stuff)
print(unique_stuff)
