# Using a nested list comprehension and range(), create a
# variable called answer with the following value:
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

answer = [[number for number in range(3)] for number in range(3)]
print(answer)
