# Using list comprehension, create a variable called answer
# with the following value:
# [
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# ]

# The answer should be a 10X10 nested list. It won't display
# formatted, it will be one giant line.

answer = [[x for x in range(10)] for x in range(10)]
print(answer)
