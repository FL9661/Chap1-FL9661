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