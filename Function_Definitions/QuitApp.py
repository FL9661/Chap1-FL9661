def Function_QuitApp():
	QuitApp = (input('(Y or N) Would you like to continue? ')).upper() # .upper forces input into upper case

	while QuitApp != '': # How to handle QuitApp Responses 
		if QuitApp == 'N':
			break
		elif QuitApp == 'Y': # if the user wishes to exit this option will close game
			import sys # importing a system function
			import time# importing a system timer function
			print('Good Bye in 5 seconds...') # prints acknowledgement output to console
			timer = 5 # start of a visible countdown timer set to 5
			while timer != 0: # if timer is not 1 run loop
				import time # import sys function
				print (timer) # prints the value of timer
				time.sleep(1) # delays next command by 1 seconds
				timer -= 1 # subtracts 1 each cycle until it reachs 1
			print ('Good Bye') # prints last message
			time.sleep(2) # delays next command by 2 seconds
			print('Closing Window.')
			sys.exit() # forces exit from Game
		elif QuitApp != 'N':
			print ('Invalid responsed detected!')
			QuitApp = (input('(Y or N) Would you like to continue? ')).upper()

Function_QuitApp()

print('continue with program.')

