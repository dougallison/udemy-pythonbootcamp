# State Abbreviations
# Given two lists `['CA', 'NJ', 'RI']` and
# `['California', 'New Jersey', 'Rhode Island']` create a
# dictionary that looks liek this:
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
# and save it to a variable called *answer*

list1 = ['CA', 'NJ', 'RI']
list2 = ['California', 'New Jersey', 'Rhode Island']

answer = {list1[i]: list2[i] for i in range(0, len(list1))}
print(answer)
