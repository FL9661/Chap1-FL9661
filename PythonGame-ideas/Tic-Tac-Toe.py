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
2 - To be able to change the board value from "-" to "X" or "O".
3 - Ensure the game can support 2 players.
4 - Vadiation to prevent Players from overwriting each others cells.

''')

delay = input ('Press Enter to continue')
clear()

Player1Confirmation = ''

player1 = input('Please enter name of Player One: ').upper()
print ('Please confirm Player One is: ', player1)

#player1 confirmation 

while Player1Confirmation != 'Y':
	Player1Confirmation = input('Please confirm Y or No: ').upper()	
	if Player1Confirmation == 'N':
		player1 = input('Please re-enter name of Player One: ').upper()
		print ('\n', 'Please confirm Player One is: ', player1, sep='')

print ('\n','                            Thank you ', player1, ' you are now Player One.', '\n', sep='')

#player2 confirmation 

Player2Confirmation = ''

player2 = input('Please enter name of Player Two: ').upper()
print ('Please confirm Player Two is: ', player2)

while Player2Confirmation != 'Y':
	Player2Confirmation = input('Please confirm Y or No: ').upper()
	if Player2Confirmation == 'N':
		player2 = input('Please re-enter name of Player Two: ').upper()
		print ('Please confirm Player Two is: ', player2, sep='')

print ('\n','                            Thank you ', player2, ' you are now Player Two.', '\n', sep='')

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
	UserChoice1= input('where would you like to insert a "X"')
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
	elif UserChoice1 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice1 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game
	
	
### Turn2 - Player 2 - Os

print(player2, end='')
delay = input (' - Turn 2: Press Enter to continue.')

clear()

print(player2,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input2 = '-'
UserChoice2 = ''

while Input2 == '-':
	print(player2, end=' ')
	UserChoice2= input('where would you like to insert a "O"?')
	elif UserChoice2 == '1':
		TTTBoard [0] [0] = 'O'
		Input2 = '1'
	elif UserChoice2 == '2':
		TTTBoard [0] [1] = 'O'
		Input2 = '1'
	elif UserChoice2 == '3':
		TTTBoard [0] [2] = 'O'
		Input2 = '1'
	elif UserChoice2 == '4':
		TTTBoard [1] [0] = 'O'
		Input2 = '1'
	elif UserChoice2 == '5':
		TTTBoard [1] [1] = 'X'
		Input2 = '1'
	elif UserChoice2 == '6':
		TTTBoard [1] [2] = '0'
		Input2 = '1'
	elif UserChoice2 == '7':
		TTTBoard [2] [0] = 'O'
		Input2 = '1'
	elif UserChoice2 == '8':
		TTTBoard [2] [1] = 'O'
		Input2 = '1'
	elif UserChoice2 == '9':
		TTTBoard [2] [2] = 'O'
		Input2 = '1'
	elif UserChoice2 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice2 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game
	
print(player1, end=' ')

### Turn3 - Player 1 - Xs

delay = input (' - Turn 3: Press Enter to continue')

clear ()

print(player1,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input3 = '-'
UserChoice3 = ''

while Input3 == '-':
	print(player1, end=' ')
	UserChoice3 = input('where would you like to insert a "X"?')
		print ('please try again, this slot has already been selected:')
	elif UserChoice3 == '1':
		TTTBoard [0] [0] = 'X'
		Input3 = '1'
	elif UserChoice3 == '2':
		TTTBoard [0] [1] = 'X'
		Input3 = '1'
	elif UserChoice3 == '3':
		TTTBoard [0] [2] = 'X'
		Input3 = '1'
	elif UserChoice3 == '4':
		TTTBoard [1] [0] = 'X'
		Input3 = '1'
	elif UserChoice3 == '5':
		TTTBoard [1] [1] = 'X'
		Input3 = '1'
	elif UserChoice3 == '6':
		TTTBoard [1] [2] = 'X'
		Input3 = '1'
	elif UserChoice3 == '7':
		TTTBoard [2] [0] = 'X'
		Input3 = '1'
	elif UserChoice3 == '8':
		TTTBoard [2] [1] = 'X'
		Input3 = '1'
	elif UserChoice3 == '9':
		TTTBoard [2] [2] = 'X'
		Input3 = '1'
	elif UserChoice3 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice3 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game

#Turn 4 - Player 2 - Os

print(player2, end='')
delay = input (' - Turn 4: Press Enter to continue.')

clear()
print(player2,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input4 = '-'
UserChoice4 = ''

while Input4 == '-':
	print(player2, end=' ')
	UserChoice4= input('where would you like to insert a "O"?')
	if  UserChoice4 == UserChoice1 or UserChoice2 or UserChoice3:
		print ('please try again, this slot has already been selected:')
	elif UserChoice4 == '1':
		TTTBoard [0] [0] = 'O'
		Input4 = '1'
	elif UserChoice4 == '2':
		TTTBoard [0] [1] = 'O'
		Input4 = '1'
	elif UserChoice4 == '3':
		TTTBoard [0] [2] = 'O'
		Input4 = '1'
	elif UserChoice4 == '4':
		TTTBoard [1] [0] = 'O'
		Input4 = '1'
	elif UserChoice4 == '5':
		TTTBoard [1] [1] = 'X'
		Input4 = '1'
	elif UserChoice4 == '6':
		TTTBoard [1] [2] = '0'
		Input4 = '1'
	elif UserChoice4 == '7':
		TTTBoard [2] [0] = 'O'
		Input4 = '1'
	elif UserChoice4 == '8':
		TTTBoard [2] [1] = 'O'
		Input4 = '1'
	elif UserChoice4 == '9':
		TTTBoard [2] [2] = 'O'
		Input4 = '1'
	elif UserChoice4 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice4 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game
	
print(player1, end='')

### Turn 5 - Player 1 - Xs

delay = input (' - Turn 5: Press Enter to continue')

clear ()

print(player1,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input5 = '-'
UserChoice5 = ''

while Input5 == '-':
	print(player1, end=' ')
	UserChoice5= input('where would you like to insert a "X"?')
	if  UserChoice5 == UserChoice1 or UserChoice2 or UserChoice3 or UserChoice4:
		print ('please try again, this slot has already been selected:')
	elif UserChoice5 == '1':
		TTTBoard [0] [0] = 'X'
		Input5 = '1'
	elif UserChoice5 == '2':
		TTTBoard [0] [1] = 'X'
		Input5 = '1'
	elif UserChoice5 == '3':
		TTTBoard [0] [2] = 'X'
		Input5 = '1'
	elif UserChoice5 == '4':
		TTTBoard [1] [0] = 'X'
		Input5 = '1'
	elif UserChoice5 == '5':
		TTTBoard [1] [1] = 'X'
		Input5 = '1'
	elif UserChoice5 == '6':
		TTTBoard [1] [2] = 'X'
		Input5 = '1'
	elif UserChoice5 == '7':
		TTTBoard [2] [0] = 'X'
		Input5 = '1'
	elif UserChoice5 == '8':
		TTTBoard [2] [1] = 'X'
		Input5 = '1'
	elif UserChoice5 == '9':
		TTTBoard [2] [2] = 'X'
		Input5 = '1'
	elif UserChoice5 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice5 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game

print(player2, end='')

### Turn 6 - Player 2 - Os

delay = input (' - Turn 6: Press Enter to continue')

clear ()

clear()
print(player2,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input6 = '-'
UserChoice6 = ''

while Input6 == '-':
	print(player2, end=' ')
	UserChoice6= input('where would you like to insert a "O"?')
	if  UserChoice6 == UserChoice1 or UserChoice2 or UserChoice3 or UserChoice4 or UserChoice5:
		print ('please try again, this slot has already been selected:')
	elif UserChoice6 == '1':
		TTTBoard [0] [0] = 'O'
		Input6 = '1'
	elif UserChoice6 == '2':
		TTTBoard [0] [1] = 'O'
		Input6 = '1'
	elif UserChoice6 == '3':
		TTTBoard [0] [2] = 'O'
		Input6 = '1'
	elif UserChoice6 == '4':
		TTTBoard [1] [0] = 'O'
		Input6 = '1'
	elif UserChoice6 == '5':
		TTTBoard [1] [1] = 'X'
		Input6 = '1'
	elif UserChoice6 == '6':
		TTTBoard [1] [2] = '0'
		Input6 = '1'
	elif UserChoice6 == '7':
		TTTBoard [2] [0] = 'O'
		Input6 = '1'
	elif UserChoice6 == '8':
		TTTBoard [2] [1] = 'O'
		Input6 = '1'
	elif UserChoice6 == '9':
		TTTBoard [2] [2] = 'O'
		Input6 = '1'
	elif UserChoice6 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice6 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game
	
print(player1, end='')

### Turn 7 - Player 1 - Xs

delay = input (' - Turn 7: Press Enter to continue')

clear ()

print(player1,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input7 = '-'
UserChoice7 = ''

while Input7 == '-':
	print(player1, end=' ')
	UserChoice7= input('where would you like to insert a "X""\?"')
	if  UserChoice7 == UserChoice1 or UserChoice2 or UserChoice3 or UserChoice4 or UserChoice5 or UserChoice6:
		print ('please try again, this slot has already been selected:')
	if UserChoice7 == '1':
		TTTBoard [0] [0] = 'X'
		Input7 = '1'
	elif UserChoice7 == '2':
		TTTBoard [0] [1] = 'X'
		Input7 = '1'
	elif UserChoice7 == '3':
		TTTBoard [0] [2] = 'X'
		Input7 = '1'
	elif UserChoice7 == '4':
		TTTBoard [1] [0] = 'X'
		Input7 = '1'
	elif UserChoice7 == '5':
		TTTBoard [1] [1] = 'X'
		Input7 = '1'
	elif UserChoice7 == '6':
		TTTBoard [1] [2] = 'X'
		Input7 = '1'
	elif UserChoice7 == '7':
		TTTBoard [2] [0] = 'X'
		Input7 = '1'
	elif UserChoice7 == '8':
		TTTBoard [2] [1] = 'X'
		Input7 = '1'
	elif UserChoice7 == '9':
		TTTBoard [2] [2] = 'X'
		Input7 = '1'
	elif UserChoice7 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice7 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game

print(player2, end='')

### Turn 8 - Player 2 - Os

delay = input (' - Turn 8: Press Enter to continue')

clear ()

print(player2,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input8 = '-'
UserChoice8 = ''

while Input8 == '-':
	print(player2, end=' ')
	UserChoice8= input('where would you like to insert a "O""\?"')
	if  UserChoice8 == UserChoice1 or UserChoice2 or UserChoice3 or UserChoice4 or UserChoice5 or UserChoice6 or UserChoice7:
		print ('please try again, this slot has already been selected:')
	elif UserChoice8 == '1':
		TTTBoard [0] [0] = 'O'
		Input8 = '1'
	elif UserChoice8 == '2':
		TTTBoard [0] [1] = 'O'
		Input8 = '1'
	elif UserChoice8 == '3':
		TTTBoard [0] [2] = 'O'
		Input8 = '1'
	elif UserChoice8 == '4':
		TTTBoard [1] [0] = 'O'
		Input8 = '1'
	elif UserChoice8 == '5':
		TTTBoard [1] [1] = 'X'
		Input8 = '1'
	elif UserChoice8 == '6':
		TTTBoard [1] [2] = '0'
		Input8 = '1'
	elif UserChoice8 == '7':
		TTTBoard [2] [0] = 'O'
		Input8 = '1'
	elif UserChoice8 == '8':
		TTTBoard [2] [1] = 'O'
		Input8 = '1'
	elif UserChoice8 == '9':
		TTTBoard [2] [2] = 'O'
		Input8 = '1'
	elif UserChoice8 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice8 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game
	
print(player1, end='')

### Turn 9 - Player 1 - Xs

delay = input ('turn 9: Press Enter to continue')

clear ()

print(player1,'this is a reminder of game coords.')
print('''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],

This is the current game state:
''')
for i in range(3): print(TTTBoard[i]) 
Input9 = '-'
UserChoice9 = ''

while Input9 == '-':
	print(player1, end=' ')
	UserChoice9= input('where would you like to insert a "X""\?"')
	if  UserChoice9 == UserChoice1 or UserChoice2 or UserChoice3 or UserChoice4 or UserChoice5 or UserChoice6 or UserChoice7 or UserChoice8:
		print ('please try again, this slot has already been selected:')
	elif UserChoice9 == '1':
		TTTBoard [0] [0] = 'X'
		Input9 = '1'
	elif UserChoice9 == '2':
		TTTBoard [0] [1] = 'X'
		Input9 = '1'
	elif UserChoice9 == '3':
		TTTBoard [0] [2] = 'X'
		Input9 = '1'
	elif UserChoice9 == '4':
		TTTBoard [1] [0] = 'X'
		Input9 = '1'
	elif UserChoice9 == '5':
		TTTBoard [1] [1] = 'X'
		Input9 = '1'
	elif UserChoice9 == '6':
		TTTBoard [1] [2] = 'X'
		Input9 = '1'
	elif UserChoice9 == '7':
		TTTBoard [2] [0] = 'X'
		Input9 = '1'
	elif UserChoice9 == '8':
		TTTBoard [2] [1] = 'X'
		Input9 = '1'
	elif UserChoice9 == '9':
		TTTBoard [2] [2] = 'X'
		Input9 = '1'
	elif UserChoice9 != 'Q' or 'q':
		print ('Please try again:')
		continue
	elif UserChoice9 == 'Q' or 'q': # if the user wishes to exit this option will close game
		import sys # importing a system function
		import time# importing a system timer function
		print('Good Bye in 5 seconds...') # prints acknowledgement output to console
		timer = 5 # start of a visible countdown timer set to 5
		while timer != 1: # if timer is not 1 run loop
			import time # import sys function
			print (timer) # prints the value of timer
			time.sleep(1) # delays next command by 1 seconds
			timer -= 1 # subtracts 1 each cycle until it reachs 1
		print ('Good Bye') # prints last message
		time.sleep(2) # delays next command by 2 seconds
		sys.exit() # forces exit from Game

print('end of game')
delay = input (' Please press Enter to finish')