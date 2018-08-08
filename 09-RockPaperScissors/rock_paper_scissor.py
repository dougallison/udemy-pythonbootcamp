import getpass

tie_game = False
winner = None
win_strategy = None
rock = 'rock'
paper = 'paper'
scissors = 'scissors'
paper_covers_rock = f'{paper} covers {rock}'
scissors_cut_paper = f'{scissors} cut {paper}'
rock_breaks_scissors = f'{rock} breaks {scissors}'
player_1 = 'player 1'
player_2 = 'player 2'


print('Welcome to Rock, Paper, Scissors!')
print('---------------------------------')
player_1_choice = getpass.getpass(f'Enter {player_1}\'s choice: ')
player_2_choice = getpass.getpass(f'Enter {player_2}\'s choice: ')
print('SHOOT!')

if(not player_1_choice or not player_2_choice):
	winner = None
elif(player_1_choice == player_2_choice):
	tie_game = True
elif(player_1_choice == rock):
	if(player_2_choice == scissors):
		win_strategy = rock_breaks_scissors
		winner = player_1
	elif(player_2_choice == paper):
		win_strategy = paper_covers_rock	
		winner = player_2
elif(player_1_choice == paper):
	if(player_2_choice == rock):
		win_strategy = paper_covers_rock
		winner = player_1
	elif(player_2_choice == scissors):
		win_strategy = scissors_cut_paper
		winner = player_2
elif(player_1_choice == scissors):
	if(player_2_choice == paper):
		win_strategy = scissors_cut_paper
		winner = player_1
	elif(player_2_choice == rock):
		win_strategy = rock_breaks_scissors
		winner = player_2

if(tie_game):
	print('TIE GAME!!!')
elif(not winner):
	print(f'Must pick from {rock}, {paper}, or {scissors}!')
else:
	print(f'{win_strategy}, {winner} wins the game!')

print('---------------------------------')