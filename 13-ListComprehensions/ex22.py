# For all the numbers between 1 and 100 (including 100), create
# a variable called answer, which contains a list with all
# the numbers that are divisible by 12.

answer = [number for number in range(1, 101) if number % 12 == 0]
print(answer)
