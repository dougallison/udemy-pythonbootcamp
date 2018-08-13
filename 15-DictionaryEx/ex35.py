# ASCII Codes Dictionary

# Every character has an ASCII code (a number that represents it).
# Python has a function called `chr()` that will return a string
# if you provide the corresponding integer ASCII code. For example:
#
# `chr(65) will return 'A'
# `chr(66) will return 'B'
# `chr(90) will return 'Z'
#
# Create a dictionary that maps ASCII keys to their corresponding
# letters. Use dictionary comprehension and `chr()`. Save the
# result to the `answer` variable.

answer = {i: chr(i) for i in range(65, 91)}
print(answer)
