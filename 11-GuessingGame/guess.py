import random

random_number = None
attempts = 0
best_score = float("inf")
while(True):
	if(not random_number):
		random_number = random.randint(1, 10)

	guess = input('Guess a number between 1 and 10: ')
	if(not guess):
		break

	guess = int(guess)
	attempts += 1
	if(guess < random_number):
		print('Too low, try again!')
	elif(guess > random_number):
		print('Too high, try again!')
	else:
		print(f'You guessed it in {attempts} attempts. You won!')
		if(attempts < best_score):
			best_score = attempts
		play_again = input('Do you want to keep playing? (y/n) ')
		if(play_again.lower() == 'n'):
			break;
		else:
			random_number = None
			attempts=0

print(f'Your best score was {best_score} attempts. Thanks for playing!')