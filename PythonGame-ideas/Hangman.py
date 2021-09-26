# Python Game Submission
# By Francis Lyness

#######################################################################################################
#                                                                                                     #
#                                   Top Level Imported Functions                                      #
#                                                                                                     #
#######################################################################################################

import os # used to import the Windows CLS command
clear = lambda: os.system('cls') # assigns Windoes CLS command to clear()
import time# importing a system timer function

#######################################################################################################
#                                                                                                     #
#                                             Game Intro                                              #
#                                                                                                     #
#######################################################################################################

# multi line print that displays a welcome output to the screen for the users

print ('''
+-----------------------------------------------------------------------------------------------------+
|                                                                                                     |
|                                 Welcome to Python Hangman                                           |
|                                                                                                     |
|                                 By 25189661 FPPL                                                    |
|                                 Code published to GitHub FL9661                                     |
|                                                                                                     |
|                                         ---------+                                                  |
|                                         |        |                                                  |
|                                         |        O                                                  |
|                                         |      --|--                                                |
|                                         |        |                                                  |
|                                         |       / \                                                 |
|                                      +-----+  +-----+                                               |
|                                      |     |  |     |                                               |
|                                      +-----+  +-----+                                               |
|                                                                                                     |
+-----------------------------------------------------------------------------------------------------+

''') # multi line print

input('Please press the Enter key to continue.') # used to hold the program until the user injects a return key strike
clear () # runs CLS command outside of the dev environment - see lines 4 & 5

#######################################################################################################
#                                                                                                     #
#                                        Do you want to play?                                         #
#                                                                                                     #
#######################################################################################################

# Basic options menu
# uses a while loop to continue, exit and provide input validation

print ('''
+-----------------------------------------------------------------------------------------------------+
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                           Would you like to play a game of hangman?                                 |
|                                                                                                     |
|                                                                                                     |
|                                        Type "Y" for Yes                                             |
|                                                                                                     |
|                                               or                                                    |
|                                                                                                     |
|                                        Type "N" to Exit                                             |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
+-----------------------------------------------------------------------------------------------------+

''')# multi line print

# Does the user wish to continue?
StartGame = (input('Please enter your answer here: ')).upper() # .upper forces input into upper case

while StartGame != 'Y': # When StartGame is not equal to Y 
	if StartGame == 'N': # if the user wishes to exit this option will close game
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

	elif StartGame != 'Y': # if user inputs any other value expect Y or N
		print('Invalid repsonse!', '\n') # outputs error message
		StartGame = (input('Please enter your answer here: ')).upper() # re-prompts user to enter response

clear () # runs CLS command outside of the dev environment - see lines 4 & 5

#######################################################################################################
#                                                                                                     #
#                                           Who is playing                                            #
#                                                                                                     #
#######################################################################################################
		
print ('''
+-----------------------------------------------------------------------------------------------------+
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                          Who is playing                                             |
|                                             Hangman?                                                |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
+-----------------------------------------------------------------------------------------------------+

''')# multi line print

Player1Confirmation = ''

player1 = input('Please enter name of Player One: ').upper()
print ('Please confirm Player One is: ', player1)

while Player1Confirmation != 'Y':
	Player1Confirmation = input('Please confirm Y or No: ').upper()	
	if Player1Confirmation == 'N':
		player1 = input('Please re-enter name of Player One: ').upper()
		print ('\n', 'Please confirm Player One is: ', player1, sep='')

print ('\n','                            Thank you ', player1, ' you are now Player One.', '\n', sep='')

Player2Confirmation = ''

player2 = input('Please enter name of Player Two: ').upper()
print ('Please confirm Player Two is: ', player2)

while Player2Confirmation != 'Y':
	Player2Confirmation = input('Please confirm Y or No: ').upper()
	if Player2Confirmation == 'N':
		player2 = input('Please re-enter name of Player Two: ').upper()
		print ('Please confirm Player Two is: ', player2, sep='')

print ('\n','                            Thank you ', player2, ' you are now Player Two.', '\n', sep='')

input('Please press the Enter key to continue.') # used to hold the program until the user injects a return key strike

clear()

#######################################################################################################
#                                                                                                     #
#                                            Confirmation                                             #
#                                                                                                     #
#######################################################################################################
		
print ('\n', '                                ', player1,' vs ', player2, '\n', sep="")

print('\n', '\n', '\n', 'Instructions for game:', '\n', player1, ' as Player 1 you will have to think of a word and a hint.', sep='')
print('Make sure that ', player2, ' cannot see your input anwser.', sep='')
print('Only enter 1 word answers, hyphenated words do not count!')

print ('\n', '                                               The Word', '\n')

word =''
Player1Confirmation = ''

word = input('Please think of a word and enter it: ').upper()
print(player1, ' you have entered: ', word, sep='')

while Player1Confirmation != 'Y':
	Player1Confirmation = input('Please confirm Y or No: ').upper()	
	if Player1Confirmation == 'N':
		word = input('Please re-enter the word: ').upper()
		print ('Please confirm the word is: ', word)

print ('\n', '                                               The Hint', '\n')

hint =''
Player1Confirmation = ''

hint = input('please think of a hint and enter it: ').upper()
print(player1, ' you have entered: ', hint, sep='')

while Player1Confirmation != 'Y':
	Player1Confirmation = input('Please confirm Y or No: ').upper()	
	if Player1Confirmation == 'N':
		hint = input('Please re-enter the hint: ').upper()
		print ('Please confirm the hint as: ', hint, sep='')

print('\n', 'Please press the Enter key to clear the screen and to stop ', player2, ' from cheating!', sep='')

input('Please press the Enter key to continue.') # used to hold the program until the user injects a return key strike

clear()