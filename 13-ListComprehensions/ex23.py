# Given the string 'amazing', create a variable called answer,
# which is a list containing all the letters from 'amazing'
# but not the vowels (a, e, i, o, and u)

answer = [letter for letter in 'amazing' if letter not in [
    'a', 'e', 'i', 'o', 'u']]
print(answer)

# Alternate solution
answer2 = [letter for letter in 'amazing' if letter not in 'aeiou']
print(answer2)
