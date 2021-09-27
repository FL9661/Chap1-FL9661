# Python Game Submission
# By Francis Lyness

#######################################################################################################
#                                                                                                     #
#                                   Top Level Imported Functions                                      #
#                                                                                                     #
#######################################################################################################

# Used for Windows Cmd Prompt CLS Command
import os # used to import the Windows CLS command
clear = lambda: os.system('cls') # assigns Windoes CLS command to clear()

# Used for Timer Function
import time# importing a system timer function

# Used with the Quit function
import sys # importing a system function

#######################################################################################################
#                                                                                                     #
#                                        Functions Definitions                                        #
#                                                                                                     #
#######################################################################################################

def Function_AnyKey():
    import msvcrt
    char = 0
    print ('Press the "Any" Key to continue...')
    while not char:
        char = msvcrt.getch() # Function_AnyKey() used for plessing any key to continue

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
			
Function_AnyKey() # calls programmer defined function
clear()

#######################################################################################################
#                                                                                                     #
#                                         Game Instructions                                           #
#                                                                                                     #
#######################################################################################################

print('''
+-----------------------------------------------------------------------------------------------------+
| Game Instructions                                                                                   |
|                                                                                                     |
| Step 1 - Set both Player Names.                                                                     |
|                                                                                                     |
| Step 2 - Set who will be the Executionor and how will be the Hangman.                               |
|                                                                                                     |
| Step 3 - The executionor will set the word and hint.                                                |
|                                                                                                     |
| Step 4 - Hangman gets to guess the secret word to win their freedom!                                |
|                                                                                                     |
| Rules - Simple no cheating:                                                                         |
|                                                                                                     |
| Hangman - No peaking when the Executionor is inputting their word.                                  |
|                                                                                                     |
| Executionor - Only set one word guesses and hyphenated words are not to be used!                    |
|                                                                                                     |
+-----------------------------------------------------------------------------------------------------+
''')

Function_AnyKey() # calls programmer defined function
clear()

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

clear()

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

player1 = input('Please enter name of Player One>>> ').upper()
print ('Please confirm Player One is. ', player1)

while Player1Confirmation != 'Y':
	Player1Confirmation = input('Please confirm Y or No. >>> ').upper()	
	if Player1Confirmation == 'N':
		player1 = input('Please re-enter name of Player One. >>> ').upper()
		print ('\n', 'Please confirm Player One is. ', player1, sep='')

print ('\n','                            Thank you ', player1, ' you are now Player One.', '\n', sep='')

Player2Confirmation = ''

player2 = input('Please enter name of Player Two. >>> ').upper()
print ('Please confirm Player Two is. ', player2)

while Player2Confirmation != 'Y':
	Player2Confirmation = input('Please confirm Y or No. >>> ').upper()
	if Player2Confirmation == 'N':
		player2 = input('Please re-enter name of Player Two. >>> ').upper()
		print ('Please confirm Player Two is ', player2, sep='')

print ('\n','                            Thank you ', player2, ' you are now Player Two.', '\n', sep='')

Function_AnyKey() # calls programmer defined function
clear()

#######################################################################################################
#                                                                                                     #
#                                            Confirmation                                             #
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
|                                      Who is the Executionor?                                        |
|                                                                                                     |
|                                    Please Enter PlayerName Now                                      |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
+-----------------------------------------------------------------------------------------------------+

''')# multi line print
Executionor =''
Hangman = ''
UserInput1 = ''

while UserInput1 == '':
	print('Press 1 for ', player1, ' or press 2 for ', player2, '. >>> ', sep='', end='')
	UserInput1 = input()
	if UserInput1 == '1':
		Executionor = player1
		print ('The Executionor is', Executionor)
		Hangman = player2
		print ('The Hangman is', Hangman)
	elif UserInput1 == '2':
		Executionor = player2
		Hangman = player1
		print ('The Executionor is', Executionor)
		print ('The Hangman is', Hangman)

print ('The Executionor is', Executionor)
print ('The Hangman is', Hangman)

print ('end of loop')

Function_AnyKey() # calls programmer defined function
clear()