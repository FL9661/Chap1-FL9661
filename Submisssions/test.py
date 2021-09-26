import os # used to import the Windows CLS command
clear = lambda: os.system('cls') # assigns Windoes CLS command to clear()

import time# importing a system timer function

print('''Tic Tac Toe

Game board should look it.

[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

Problems
1 - Print a 2 dimenisal game board.
2 - To be able to change 1 value from - to X or O
3 - Who is the players

''')

delay = input ('Press Enter to continue')
clear()

Player1Confirmation = ''

player1 = 'me'
player2 = 'Gemma'

delay = input('Please press the Enter key to continue.') # used to hold the program until the user injects a return key strike
clear ()

### Turn1 - Player 1 - Xs

print(player1,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')

TTTBoard = [["-"for i in range(3)] for j in range(3)] #create complete board
EMPTY = '-'

for i in range(3): print(TTTBoard[i]) #print complete board

Input1 = '-'
UserChoice1 = ''

while Input1 == '-':
	print(player1, end=' ')
	UserChoice2= input('where would you like to insert a "X"? ')
	if UserChoice1 == '1':
		TTTBoard [0] [0] = 'X'
		Input1 = '1'
	elif UserChoice1 == '2':
		TTTBoard [0] [1] = 'X'
		Input1 = '1'
	elif UserChoice1 == '3':
		TTTBoard [0] [2] = 'X'
		Input1 = '1'
	elif UserChoice1 == '4':
		TTTBoard [1] [0] = 'X'
		Input1 = '1'
	elif UserChoice1 == '5':
		TTTBoard [1] [1] = 'X'
		Input1 = '1'
	elif UserChoice1 == '6':
		TTTBoard [1] [2] = 'X'
		Input1 = '1'
	elif UserChoice1 == '7':
		TTTBoard [2] [0] = 'X'
		Input1 = '1'
	elif UserChoice1 == '8':
		TTTBoard [2] [1] = 'X'
		Input1 = '1'
	elif UserChoice1 == '9':
		TTTBoard [2] [2] = 'X'
		Input1 = '1'
	
