player1 = 'Francis'
player2 = 'You'

Executionor =''
Hangman = ''
UserInput1 = ''

while UserInput1 == '':
	print('Press 1 for ', player1, ' or press 2 for ', player2, '. >>> ', sep='', end='')
	UserInput1 = input()
	if UserInput1 == '1':
		Executionor = player1
		Hangman = player2
	elif UserInput1 == '2':
		Executionor = player2
		Hangman = player1
		print ('The Executionor is', Executionor)
		print ('The Hangman is', Hangman)

print ('The Executionor is', Executionor)
print ('The Hangman is', Hangman)