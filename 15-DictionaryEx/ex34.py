# Vowels Dict Exercise

# Create a dictionary with the key as a vowel in the alphabet
# and the value as zero. The dictionary should look like:
# `{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}`

# Use dictionary comprehension or a dict method

answer = {k: 0 for k in 'aeiou'}
print(answer)

# alternative solution
answer = dict.fromkeys('aeiou', 0)
print(answer)
