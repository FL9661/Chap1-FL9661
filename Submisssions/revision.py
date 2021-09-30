########## print functions ##########
# sep="" replaces the comma separator
# end="" replaces the new line separator "\n"
# using print ("text"*2) will print text twice on same line
print ("""
multi line outputs
""")

########## var functions ##########
string = "text"
variable = 1
print (float(variable))
print (int(variable))
print (string, variable)
a = 1
b = 2
print (a, b)
print (a + b)
print (a - b)
print (a / b)
print (a * b)
print (round(a / b))
# // floor division
# % whats left over
# round +num 0.5 rounds down to .0
# round -num -0.5 rounds to -1

########## input functions ##########
varStr = input("printed text goes here") #input function

varInt = int(input("please insert num and sets as a Int Number"))
print (varInt)
varfloat = float(input("lease insert num and sets as a Float Number"))
print (varfloat)
uppercase = input("enter test").upper # converts text case to Uppercase
lowercase = input("enter test").lower # converts text case to Uppercase

# 2.6.1.10 Lab
x = float(input("Enter value for x: "))
y = float(1/(x+1/(x+1/(x+1/(x))))) #start from bottom of formula, bracket and then work backwards
print("y =", y, "\n")

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
# outputs 55555

x = input("Enter a number: ") # The user enters 2
print(type(x))
#outputs str

########## Lists ##########
blanklist = []
mylist = [1,2,3,4]
print ("whole list", mylist)
print ("second list value [1:2]", mylist[1:2]) #prints index values 1 only
print ("second list value [1:-1]", mylist[1:-1]) #prints index values 1 onwards
print ("second list value [1:3]", mylist[1:3]) #prints index values 1 only
print ("second list value [1:]", mylist[1:]) #prints index values 1 onwards
print ("second list value [1:4]", mylist[1:4]) #prints index values from 1 onwards
print ("second list value [1:len(mylist)]", mylist[1:len(mylist)]) #prints index values from 1 onwards
print ("second list value [1:0]", mylist[1:0]) #prints index []
print ("mylists length is:", len(mylist))
my_list = []
my_list.insert (0, 5) # (i, x) inserst value (x) at i and shifts list to the the right
del my_list [3] # deletes the value at a specific index
my_list.append (6) # adds a new value at the end of the list
my_list[0], my_list[4] = my_list[4], my_list[0] # swaps the list values using index numbers

# table within a table
t= [[3-i in range(3)] for j in range (3)]
s = 0
for i in range (3)
    s += t[i] [i]
print (s) # output 6 

#totals
my_list = [1,2,3,4]
total = 0
for i in range(len(my_list)): # for each index with the range
    total += my_list[i] # total = 0 + i0 +i1 + i2 + i3
print(total)

# copying lists
mylist = [4, 6, 8, 10, 12, 14]
print(mylist)
newlist = mylist [:]
print (newlist)

# incrementing a blank list
my_list = []
var = 2
while var <= 22:
    var += 2
    my_list.append(var)
print (my_list) 

# incrementing an existing list
my_list = []
var = 2
while var <= 20:
    var += 2
    my_list.append(var)
print (my_list)
length = (len(my_list))
print (length)

for i in range (length):
    if True:
        var = my_list[i]*3
        my_list.append(var)
print (my_list)

for i in range (length):
    if True:
        del my_list[0]
print(my_list)

########## Bubble Sorting Lists ##########
my_list = ["b", "e", "a", "g", "z"]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

lst = [5, 3, 1, 2, 4]
print(lst)
lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]

lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

########## if and elif statements ##########
Val1 = int(input("insert Val1 now: "))
if Val1 == 0:
    print ("this is nothing")
elif Val1 < 0:
    print ("this is a negative number")
else:
    print("this is a postive number")

########## if, elif and else statements ##########
varInt = int(input("please insert and Int Number: "))
if varInt == 0:
    print ("please type a whole nmber value!")
    varInt = int(input("please insert and Int Number: "))
elif varInt <= 100:
     print ("Boollean Value is ", varInt <= 100)
     print ("this number is equal to or less than 100")
elif varInt > 100:
     print ("Boollean Value is ", varInt > 100)
     print ("this number is greater than 100")

########## While True ##########
secret_letter = 'Y'
guess = input('Please guess the secret letter: ') # users input of there guess word.
while True:
    if guess != secret_letter: # If guess is not equal to secret_letter - rechallenge user
        guess = input('Please guess the secret letter: ') # rechallenge user
    if  guess == secret_letter: # If guess is equal to secret_letter
        break # exit loop then start at next print function
print ('You\'ve successfully left the loop.')

########## While Loop ##########
Loop1 = 1 # Start Value
while Loop1 <= 10: # do this until Loop1 is <= 10
    print ("Loop1>>>", Loop1) # prints current Loop1 Value 
    Loop1 += 1 # +1 to the loop value on each cycle:
    if Loop1 > 10:
       print ("While Loop \"Loop 1\" Complete")

# while loop incrementing a
my_list = []
var = 2
while var <= 22:
    var += 2
    my_list.append(var)
print (my_list)    

########## Program Define Functions ##########

#bmi count
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2
print(bmi(352.5, 1.65))

# Tax Calc
def calc(Wage, OpUserTax):
    while True:    
        if OpUserTax == "Y":
            UserTaxPrecentage=int(input("Tax amount: "))
            UserTaxTotal = ((UserTaxPrecentage/100)*Wage)
            print (Wage-UserTaxTotal)
        elif OpUserTax == "N":
            DefaultTaxPrecentage = 20 # makes this var accessable outside the scope of this defined function
            DefaultTaxTotal = ((DefaultTaxPrecentage/100)*Wage)
            print (Wage-DefaultTaxTotal)
            break
        elif OpUserTax != "N":
            OpUserTax = input("Do you want to enter your Tax amount? Y/N >>> ")
calc(Wage=int(input("Wage amount: ")), OpUserTax = input("Do you want to enter your Tax amount? Y/N >>> ").upper())

# is a triangle?
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# 4.5.1.9 Exercise
def fun(a):
    if a > 30:
        return 3 #  3
    else:
        return a + fun(a + 3) # 25 + (25+3) =53

print(fun(25)) # outputs 56

########## Tuples ##########
emptytuple = ()
tuple_1 = (1, 2, 4, 8) # written with round brackets
print(tuple_1) # outputs (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125 # and or without brackets
print(tuple_2) # output (1., 0.5, 0.25, 0.125)
one_element_tuple_1 = (1, )
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])# output 1
print(my_tuple[-1]) # output 1000
print(my_tuple[1:]) # output 10, 100, 1000
print(my_tuple[:-2])# output 1, 10
for elem in my_tuple:
    print(elem) # outputs each number 1 per line
print(len(tuple_1)) # outputs length
print(10 in my_tuple) # if in True if not False
print(-10 not in my_tuple) # if present outputs True, if present outputs false
tuplename = tuple(my_list)
del tuple_1
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]

########## Dictrionaries ##########
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
print(dictionary) # {'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
print(phone_numbers) # {'Suzy': 5557654321, 'boss': 5551234567}
print(empty_dictionary # {}
print(dictionary['cat']) # chat
print(phone_numbers['Suzy']) # 22657854310
# the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
# modify dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['cat'] = 'minou' 
print(dictionary) # {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}


# compairing
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
#outputs 
# cat -> chat
# lion is not in dictionary
# horse -> cheval

# print matches
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for english, french in dictionary.items():
    print(english, "->", french)

# 4.6.1.9 Tuples and dictionaries
school_class = {}
while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

#line 1: create an empty dictionary for the input data; the student's name is used as a key, while all the associated scores are stored in a tuple (the tuple may be a dictionary value - that's not a problem at all)
#line 3: enter an "infinite" loop (don't worry, it'll break at the right moment)
#line 4: read the student's name here;
#line 5-6: if the name is an empty string (), leave the loop;
#line 8: ask for one of the student's scores (an integer from the range 0-10)
#line 9-10: if the score entered is not within the range from 0 to 10, leave the loop;
#line 12-13: if the student's name is already in the dictionary, lengthen the associated tuple with the new score (note the += operator)
#line 14-15: if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score;
#line 17: iterate through the sorted students' names;
#line 18-19: initialize the data needed to evaluate the average (sum and counter)
#line 20-22: we iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
#line 23: evaluate and print the student's name and average score.

#merging lists to dictionaries
mylist1 = ["food1", "food2"]
mylist2 = [1.99,  6.99]
pricing_dictionary = dict(zip(mylist1, mylist2)) # {'food1': 1.99, 'food2':6.99}
print (pricing_dictionary)