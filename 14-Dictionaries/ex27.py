# Given the dictionary below:
#
# artist = {
#	'first': 'Neil',
#	'last': 'Young'
# }
#
# Declare a variable called full_name that is equal to
# artist's first and last names with a space between.

artist = {
    'first': 'Neil',
    'last': 'Young',
}

# Using string concatenation
full_name = artist['first'] + ' ' + artist['last']
print(full_name)

# Using Format()
full_name = '{} {}'.format(artist['first'], artist['last'])
print(full_name)

# Using f-string (won't work in < Python 3.6)
full_name = f"{artist['first']} {artist['last']}"
print(full_name)
