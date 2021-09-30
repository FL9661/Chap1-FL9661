# F Lyness #

# Chap 2-6 using input functions

# 2.6.1.9 Lab - using float value variables
a = float(input('Please insert the value for "a": '))
b = float(input('Please insert the value for "b": '))
print('a+b=', a + b)
print('a-b=', a - b)
print('a*b=', a * b)
print('a/b=', a + b, '\n')

# 2.6.1.10 Lab - finding the value of y
x = float(input('Enter value for x: '))
y = float(1/(x+1/(x+1/(x+1/(x))))) #start from bottom of formula, bracket and then work backwards
print('y =', y, '\n')

# 2.6.1.11 Lab - expected finish time calculator
hour = int(input('Starting time (hours): ')) #User input for hours
mins = int(input('Starting time (minutes): ')) #User input for mins
dura = int(input('Event duration (minutes): ')) #User input for duration in mins

HH = int((hour * 60 + mins + dura)//60) #Converts time inputs in minutes and outputs hours to zero decimal places
MM = int((hour * 60 + mins + dura)%60) #Converts time inputs in minutes, outputs remainder to zero decimal places for mins
print (HH % 24, ':', MM, sep='') # %24 outputs the remainder of HH when devided by 24 clock times

# Chap 3-1 using comparison operators

# 3.1.1.4 Lab - varible input comparison to fixed falue
var = int(input('Please input a numerical value: ')) #user has to input a whole number
print (var >= 100) # returns a value of false if input value is less than 100

# 3.1.1.9 Lab - Comparison operators and conditional execution based on 3 user inputs
plant = (input ('Please type plant name: ')) #initial user input creates plant var value
if plant == 'SPATHIPHYLLUM': #plant var value compaired against pre-defined value 1
	print ('"Yes - Spathiphyllum is the best plant ever!"') # if match print text on console
else: # if pre-defined value does not match check var aginst
	if plant == 'spathiphyllum': # pre-defined value 2
		print ('"No, I want a big Spathiphyllum!"') # if match print text on console
	else: # if pre-defined value 1 & 2 does not match check var aginst
		if plant == 'Spathiphyllum':
			print ('"Spathiphyllum! Not [input]!"') # if match print text on console

# 3.1.1.10 Lab - if-else statements
income = float(input("Enter the annual income: "))
tax = 0
if income == 0:
    print ('Get a job and start paying taxes.')
else:
    if income <= 85528: #85528 and below = low tax band
        tax = ((income * 0.18)- 556.02)# lower tax rate @ 18% + tax relief)
        print ('low income bracket') # denotes tax band to user
    else:
        if income >= 85528.01: #85528 above = higer tax band
            tax = ((income -85528)*0.32 + 14839) # higher tax earning @ 32% + 18% tax allowance
            print ('higher income tax bracket') # denotes tax band to user
tax = round(tax, 0)
if tax <= 0: # prevents a negative tax value being return
    print ('The tax is:', 0, 'thalers not enought taxable income') 
else:
    if tax > 0:
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

# 3.2.1.10 Lab - Ugly Vowel Eater

user_word = input('Please enter your word now: ')#user input
user_word = user_word.upper()

for letter in user_word: # If a letter within var user_word: 
    if letter == 'A': # Lines 42-50 can be replaced with "if letter in 'AEIOU':""
        continue # does not print letters containing 'A'
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter) # prints 1 letter per line, use print (letter, end="") to present all letters on a single line.
        
# 3.2.1.11 Lab - Pretty Vowel Eater

user_word = input('Please enter your word now: ')
user_word = user_word.upper()
word_without_vowels = '' # empty var 

for letter in user_word:
    if letter in 'AEIOU': # removes elif statement requirements
        continue
    else:
        word_without_vowels = word_without_vowels + letter # empty var + letter outputs after loop outputs
# lines 65 + 67 can be replaced with "print (letter, end="")"
print (word_without_vowels) #prints program output on a single line

### 3.2.1.14 - building pyramid blocks  - HELP NEEDED HERE ###
blocks = int(input("Enter the number of blocks: "))
height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1
print("The height of the pyramid:", height)
#YouTube help used but I still did not understand

# F Lyness
# Date 23 Sept 2021

# Lab 3.4.1.6: the basics of lists #
# Task: use a list to print a series of numbers 

hat_numbers = [1,2,3,4,5]
#list containing each number value known as an element
print ('There once was a hat. The hat contained no rabbit, but a list of five numbers: ', hat_numbers [0], hat_numbers [1], hat_numbers [2], hat_numbers [3], 'and', hat_numbers [4])
# prints each element value using its index numeber
hat_numbers [3] = input('Please assign new number value: ')
# step 1 prompt the user to replace the middle element value
del hat_numbers [-1]
# removes the last element from the list (Step 2)
print ('number of list entries is: ', len(hat_numbers))
#outputs to the console number of elements within the list 

# Lab 3.4.1.13: the Beatles #
# step 1 create an empty list named beatles;
beatles = [] # name of list = [] empty element container
print('Step 1:', beatles) # Outputs list elemetns to console 
# step 2 - Add first memebr elements
beatles.append('John Lennon') #0
beatles.append('Paul McCartney') #1
beatles.append('George Harrison') #2
print('Step 2:', beatles) # Outputs list elemetns to console 
# step 3 - input new memebr elements
a = input ('enter Pete Best: ')
b = input ('enter Stu Sutcliffe: ')
for i in beatles: 
    if a == ('Pete Best'):
        beatles.append (a)
    if b == ('Stu Sutcliffe'):
        beatles.append (b)
        print('Step 3:', beatles)
        break
# step 4 - remove old memebr elements
del beatles [4] # Del George Harrison
del beatles [3] # Del Stu Sutcliffe
#Step 5
beatles.insert(0, 'Ringo Star')
print('step 4:', beatles)


# Lab 3.6.1.9 - copying uniques numbers to a new list

Forename = input('Please enter your Forename: ') # users firstname
Surname = input('Please enter your Forename: ') # users surname
mylist = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]#current list
newlist = [] #new blank list

print('Hello', Forename, Surname, 'I have taken your old list that contained')
print('these values ', mylist, '.', '\n', '\n', sep='' )

for i in mylist: #for numbers within mylist
        if i not in newlist: #if i is unique not in newlist
            newlist.append (i) # add i to new list

print('I have made a new list that has', (len(newlist)), 'unique instances. These instances are:')
print (newlist)

# Lab 4.3.1.6 A leap year: writing your own functions

def is_year_leap(year):
    if (year) < 1582:
        print ('Not within the Gregorian calendar period.')
        return False
    elif (year % 4 ) != 0: # if output is not equal to 0 = common year
        print ("common year")
        return False
    elif (year % 100 ) != 0: # if output is not equal to 0 = leap year
        print ("leap year")
        return True
    elif (year % 400 ) != 0: # if output is not equal to 0 = common year
        print ("common year")
        return False
    else:
        print ("leap year") # everything else is a leap year
        return True
    
test_data = [1581, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Lab 4.3.1.7 How many days: writing and using your own functions
def is_year_leap(year):# From Lab 4.3.1.6 deleted additional print outputs
    if (year % 4 ) != 0: # if output is not equal to 0 = common year
        return False
    elif (year % 100 ) != 0: # if output is not equal to 0 = leap year
        return True
    elif (year % 400 ) != 0: # if output is not equal to 0 = common year
        return False
    else:
        return True
### I had to light blub this part as I was completely lost, I do not understand how the res value works
def days_in_month(year,month):
	# if statement
		# ...
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res
### Test data
test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr,mo,"-> ",end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Lab 4.3.1.10 : Converting fuel consumption

def liters_100km_to_miles_gallon(litres):
    km_per_litres = 100 / litres  #100/litres = km per litre 25.64
    miles_per_litre = km_per_litres / 1.609344 # miles per litre
    gallon = 3.785411784 #litres
    miles_per_gallon = miles_per_litre * gallon
    return miles_per_gallon
    
def miles_gallon_to_liters_100km(miles):
    mile2km = 1 * 1.609344 # 1.62137119223733396961743418436332
    gallon = 3.785411784 #litres
    total_Km_Per_Gallon = miles * mile2km #= 97.0434432
    Km_Per_litre = total_Km_Per_Gallon / gallon # 25.636165558045401805089324464363 km per litre
    litres_to_100km = 100 / Km_Per_litre
    return 'litres to 100Km: ', litres_to_100km # not sure why this now prints an additional () with brackets and is brackets used it returns an additional none line
   
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

###Expected Output
# 0.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
#10.009131205673757

def intro(a=input('first name: '), b=input('last name :')):
    print("My name is", a , b)

intro()