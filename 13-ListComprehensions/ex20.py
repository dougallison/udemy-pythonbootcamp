# Given a list ['Elie', 'Tim', 'Matt'], create a variable called
# answer, which is a new list containing the first letter of each
# name in the list.

answer = [name[0] for name in ['Elie', 'Tim', 'Matt']]
print(answer)


# Given a list [1,2,3,4,5,6], create a new variable called
# answer2, which is a new list of all the even values.

answer2 = [number for number in range(1, 7) if number % 2 == 0]
print(answer2)
