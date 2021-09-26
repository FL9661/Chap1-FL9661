player1= 'Francis'
player2 = 'Gemma'

Executionor = ''
Hangman = ''
UserConfirmation1 = ''

print('Press 1 for ', player1, ' or press 2 for ', player2, '. >>> ', sep='', end='')
UserInput1 = input('').upper

while UserInput1 != False:
	if Executionor == '1':
		Executionor = player1
		print ('The Executionor is', Executionor)
		Hangman = player2
		print ('The Hangman is', Hangman)
	elif UserInput1 == '2':
		Executionor = player2
		Hangman = player1
		print ('The Executionor is', Executionor)
		print ('The Hangman is', Hangman)

print ('end of loop')
