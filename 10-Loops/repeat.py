exitPhrase = 'stop copying me'
answer = input('Hey how\'s it going? ')

while(answer and answer.lower() != exitPhrase):
	answer = input(f'{answer}\n')

print('UGH FINE YOU WIN')
