# Given two lists [1,2,3,4] and [3,4,5,6] create a variable called
# answer, which is a new list that is the intersection of the two.
# Output should be [3,4].

answer = [x for x in range(1, 5) if x in range(3, 7)]
print(answer)

# Given a list of words ['Elie', 'Tim', 'Matt'] create a variable
# called answer2 which is a new list with each word reversed and
# in lower case

answer2 = [person[::-1].lower() for person in ['Elie', 'Tim', 'Matt']]
print(answer2)
