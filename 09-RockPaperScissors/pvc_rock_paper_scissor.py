import getpass
import random

tie_game = False
winner = None
win_strategy = None
rock = 'rock'
paper = 'paper'
scissors = 'scissors'
paper_covers_rock = f'{paper} covers {rock}'
scissors_cut_paper = f'{scissors} cut {paper}'
rock_breaks_scissors = f'{rock} breaks {scissors}'
player_1 = 'player'
player_2 = 'computer'


print('Welcome to Rock, Paper, Scissors!')
print('---------------------------------')
player_choice = getpass.getpass(f'Enter your move: ')
if(player_choice):
	player_choice = player_choice.lower()

ai_choice = random.randint(0, 2)
if(ai_choice == 0):
	ai_choice = rock
elif(ai_choice == 1):
	ai_choice = paper
elif(ai_choice == 2):
	ai_choice = scissors

print('SHOOT!')

if(not player_choice or not ai_choice):
	winner = None
elif(player_choice == ai_choice):
	tie_game = True
elif(player_choice == rock):
	if(ai_choice == scissors):
		win_strategy = rock_breaks_scissors
		winner = player_1
	elif(ai_choice == paper):
		win_strategy = paper_covers_rock	
		winner = player_2
elif(player_choice == paper):
	if(ai_choice == rock):
		win_strategy = paper_covers_rock
		winner = player_1
	elif(ai_choice == scissors):
		win_strategy = scissors_cut_paper
		winner = player_2
elif(player_choice == scissors):
	if(ai_choice == paper):
		win_strategy = scissors_cut_paper
		winner = player_1
	elif(ai_choice == rock):
		win_strategy = rock_breaks_scissors
		winner = player_2

if(tie_game):
	print(f'Both players choose {player_choice}, TIE GAME!!!')
elif(not winner):
	print(f'Must pick from {rock}, {paper}, or {scissors}!')
else:
	print(f'{player_1} chooses {player_choice}, {player_2} chooses {ai_choice}')
	print(f'{win_strategy}, {winner} wins the game!')

print('---------------------------------')