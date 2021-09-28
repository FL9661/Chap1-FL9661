# Lab 2.1.1.6
# display and ouput text console
print("Hello, Python!")

# Lab 2.1.1.6 - Error Messages
print("Hello, Python!")
print ("Francis")
print ("Step 3 - NameError: name 'francis' is not defined")# remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
print ("Step 4 - SyntaxError: Missing parentheses in call to 'print'. Did you mean print(\"francis\")?") # Remove parentheses error

# Lab 2.1.1.18 - using seperators and end 
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

# Lab 2.1.1.19 Formatting the output using the *, "\n" and sep="" code
print("         *           "*2, "\n", "        * *          "*2, "\n", "       *   *         "*2, sep="")
print("      *     *        "*2, "\n", "     *       *       "*2, "\n", "    *         *      "*2, sep="")
print("   *           *     "*2, "\n", "  *             *    "*2, "\n", " *               *   "*2, sep="")
print("******       ******  "*2, "\n", "     *       *       "*2, "\n","     *       *       "*2, "\n","     *       *       "*2, "\n","     *       *       "*2, sep="")
print("     *********       "*2)

# Lab 2.2.1.11 Python Literals - Strings with double quotes
print("\"I'm\"", "\n", "\"learning\"", "\n", "\"Python\"", sep="")
print("\n")

# Lab 2.4.1.7 Variables
# Step 1
Var1 = ("John")
Var2 = ("Mary")
Var3 = ("Adam")
# Step 2
John = 3 
Mary = 5
Adam = 6 
# Step 3
print (John, Mary, Adam, "\n", sep=", ")
# Step 4
total_apples = John + Mary + Adam
print ("total_apples = John + Mary + Adam", "\n")
# Step 5
print ("total_apples =", total_apples, "\n")

# Lab 2.4.1.9 Variables: a simple converter
kilometers = 12.25
miles = 7.38
miles_to_kilometers = (miles * 1.61)
kilometers_to_miles = (kilometers / 1.61)
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers") #rounds Varabile to a specified decimal place 
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles", "\n")

# Lab 2.4.1.10 Operators and expressions
x =  -1
x = float(x)
y = ((3 * x **3)-(2 * x **2)+(3 * x)-1) #3times x by the power of
print("y =", y, "\n")

# Lab 2.51.2 Comments
# this program computes the number of seconds in a given number of hours
# Program has been written 20 Sept 2021
a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", a) # Prints predefined variable of the number of hours
print("Hours in Seconds: ", a * seconds) # multiplies the number of hours by the number of seconds of an hour
print ("Goodbye")
#this is the end of the program that computes the number of seconds in 2 hour

# Lab 3.1.1.4 Questions and answers
# 3.1.1.4 Lab - varible input comparison to fixed falue
var = int(input("Please input a numerical value: ")) #user has to input a whole number
print (var >= 100) # returns a value of false if input value is less than 100

# Lab 3.1.1.10 - Comparison operators and conditional execution
plant = (input ("Please type plant name: ")) #initial user input creates plant var value
if plant == "SPATHIPHYLLUM": #plant var value compaired against pre-defined value 1
	print ("\"Yes - Spathiphyllum is the best plant ever!\"") # if match print text on console
else: # if pre-defined value does not match check var aginst
	if plant == "spathiphyllum": # pre-defined value 2
		print ("\"No, I want a big Spathiphyllum!\"") # if match print text on console
	else: # if pre-defined value 1 & 2 does not match check var aginst
		if plant == "Spathiphyllum":
			print ("\"Spathiphyllum! Not [input]\"") # if match print text on console.


# Lab 3.1.1.11 - if-else statements
income = float(input("Enter the annual income: "))
tax = 0

if income == 0:
    print ("Get a job and start paying taxes nai!")
else:
    if income <= 85528: #85528 and below = low tax band
        tax = ((income * 0.18)- 556.02)# lower tax rate @ 18% + tax relief)
        print ("low income bracket") # denotes tax band to user
    else:
        if income >= 85528.01: #85528 above = higer tax band
            tax = ((income -85528)*0.32 + 14839) # higher tax earning @ 32% + 18% tax allowance
            print ("higher income tax bracket") # denotes tax band to user
tax = round(tax, 0)
if tax < 0: # prevents a negative number return
    print ("The tax is:", 0, 'thalers not enought taxable income') 
else:
    if tax >0.01:
        print ('The tax is:', tax, 'thalers')

# Lab 3.1.1.12 LAB: Essentials of the if-elif-else statement
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

# Lab 3.2.1.3 Essentials of the while loop - Guess the secret number

# Lab 3.2.1.9 The break statement - Stuck in a loop

# Lab 3.2.1.10 The continue statement - the Ugly Vowel Eater

# Lab .2.1.11 The continue statement - the Pretty Vowel Eate

# Lab 3.2.1.14 Essentials of the while loop

# Lab 3.2.1.15 Collatz's hypothesis

# Lab 3.4.1.6 The basics of lists

# Lab 3.4.1.13 The basics of lists - the Beatles

# Lab 3.6.1.9 LAB: Operating with lists - basics

# Lab building a 2D tic-tac-toe game

# Lab 4.3.1.6 A leap year: writing your own functions

# Lab 4.3.1.7 How many days: writing and using your own functions

# Lab 4.3.1.8 Day of the year: writing and using your own functions

# Lab 4.3.1.9 Prime numbers - how to find them


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

# Dictionary help resolution example
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# adding to a tuple
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.update({"duck": "canard"})
print(dictionary)

#Gluing two Tuples
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
for item in (d1, d2):
    d3.update(item)
print(d3)

#counting duplciates in tuples
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)    # outputs: 4

#Converting a tuple into a dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)

#Copy Tuple to Tuple
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)