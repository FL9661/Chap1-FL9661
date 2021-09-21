# Chap 3-1 using comparison operators

# 3.1.1.4 Lab - varible input comparison to fixed falue
var = int(input('Please input a numerical value: ')) #user has to input a whole number
print (var >= 100) # returns a value of false if input value is less than 100

# 3.1.1.10 Lab - Comparison operators and conditional execution
plant = (input ('Please type plant name: ')) #initial user input creates plant var value
if plant == 'SPATHIPHYLLUM': #plant var value compaired against pre-defined value 1
	print ('"Yes - Spathiphyllum is the best plant ever!"') # if match print text on console
else: # if pre-defined value does not match check var aginst
	if plant == 'spathiphyllum': # pre-defined value 2
		print ('"No, I want a big Spathiphyllum!"') # if match print text on console
	else: # if pre-defined value 1 & 2 does not match check var aginst
		if plant == 'Spathiphyllum':
			print ('"Spathiphyllum! Not [input]!"') # if match print text on console

# 3.1.1.11 Lab - if-else statements
income = float(input("Enter the annual income: "))
tax = 0

if income == 0:
    print ('Get a job and start paying taxes nai')
else:
    if income <= 85528: #85528 and below = low tax band
        tax = ((income * 0.18)- 556.02)# lower tax rate @ 18% + tax relief)
        print ('low income bracket') # denotes tax band to user
    else:
        if income >= 85528.01: #85528 above = higer tax band
            tax = ((income -85528)*0.32 + 14839) # higher tax earning @ 32% + 18% tax allowance
            print ('higher income tax bracket') # denotes tax band to user

tax = round(tax, 0)
if tax < 0: # prevents a negative number return
    print ('The tax is:', 0, 'thalers not enought taxable income') 
else:
    if tax >0.01:
        print ('The tax is:', tax, 'thalers')

# 3.1.1.12 Lab - if-else statements
year = int(input('Enter a year: '))

if year < 1582: # excludes years pre-dating Gregorian calendar
    print ('Not within the Gregorian calendar period.') # outputs to console that input is invalid
else:
    if (year % 4 ) != 0: # if output is not equal to 0 = common year
       print ('common year') 
    elif (year % 100 ) != 0: # if output is not equal to 0 = leap year
       print ('leap year')
    elif (year % 400 ) != 0: # if output is not equal to 0 = common year
       print ('common year')
    else:
        print ('leap year') # everyelse is a leap year
