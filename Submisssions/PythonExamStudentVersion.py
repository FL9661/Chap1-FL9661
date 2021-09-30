##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Francis Lyness
##Course Number: SIMR 20/001
##Student Number: 25189661

#####################################################
#Section 1 25 Marks

#1) Create and Assign a type float variable called fltOne the value 10 (3)
fltOne = float(10)

#2) Create and Assign a type float variable called fltTwo the value 20 (3)
fltTwo = float(20)

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = fltOne * fltTwo

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "

#5) On the console, output stringOne and fltThree (in that order) (3)
print (stringOne, fltThree)

#6) increment fltOne  (3)
fltOne = fltOne + 1

#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)
fltTwo = float(input("Please provide another number for fltTwo"))

#8) on the console, output the product of fltOne and flotTwo with a suitable message (3) 
print ("The product of fltOne (", fltOne, ") and fltTwo (", fltTwo, ") is ", fltOne * fltTwo, sep="")

#####################################################
#Section 2 35 Marks

#8) take the input from fltTwo and apply a decision based on the number inputted . 
#The decision should be based on if the user inputs a number below 100 
#the code should output "below 100" (5)
fltTwo = (input("Please provide another number for fltTwo "))
fltTwo = int(fltTwo)
if fltTwo <= 99:
        print ("below 100")

#9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
#Using if, else and elif, output the following: 
Val1 = fltOne - fltTwo
if Val1 == 0:
    print ("value is zero")#if the product is 0 output "value is zero"
elif Val1 < 0:
    print ("below 0")#If the product is below 0, output "below 0"
else:
    print("above 0")#if the product is above 0 output "above 0" (8)

#10) create a list called listOfInts (4)
listOfInts = []

#11 part a) create a for loop to iterate through the above list and populate the list with 
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)
var = 2
while var <= 20:
    var += 2
    listOfInts.append(var)
print ("listOfInts starting at 4 incrementing in 2s:", listOfInts)

#11 part b) create a for loop to iterate through the above list and 
#multiply each value by three assigning the new value to the respective 
#index in the list. The list should now look like {12,18,24.....} (8)
length = (len(listOfInts))
for i in range (length):
    if True:
        var = listOfInts[i]*3
        listOfInts.append(var)

for i in range (length):
    if True:
        del listOfInts[0]

#11 part c )output listOfInts to the screen with a suitable message (3)
print("ListOfInts starting at 4 incrementing in 2s then multiplied by 3:", listOfInts)

#####################################################
#Section 3 20 marks

#14) create a function which calculates a decrease of a given percentage (10 marks)
def calcPerc(Cost, Percentage):# the function should be called calcPerc
    global Gvar# makes this var accessable outside the scope of this defined function
    if Percentage == "":
        Percentage = 10 #The percentage value should assume 10% if no value is given
    Percentage = int(Percentage)
    UserTotal = ((Percentage/100)*Cost)#For example if the paramenters are cost = 100 and percentage = 50, it should return 50. 
    print (Cost-UserTotal)#it should return the cost less the percentage amount
    Gvar = (Cost-UserTotal)

Cost = int(input("Please ent the cost: "))
Percentage = input("Please ent the percentage: ")

calcPerc(Cost, Percentage)
print("Global var: ",Gvar)

print ("Printing a test to the screen with cost set as 50 and percentage set as 10: ", end ="")#print a test to the screen with cost set as 50 and percentage set as 10
calcPerc(Cost = 50, Percentage = 10) #print a test to the screen with cost set as 50 and percentage set as 10

#15)
def caseChanger(word):
    word = word.lower()
    for letter in word: # If a letter within var user_word: 
        if letter == 'e':
            print ("E", sep="", end="")#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
            continue
        else:
            print(letter, sep="", end="") # prints 1 letter per line, use print (letter, end="") to present all letters on a single line.
    print() # required to stop next text 
caseChanger(word=str(input("Please enter your word here: "))) # create a function called caseChanger which takes a string argument written all in lower case
#Perform a test print which using hello: caseChanger("hello") this should

caseChanger(word="hello")
#print hEllo to the console.

##################################################### 
#Section 4 20 marks

#16)
#a) Create a list that represents a set of students. The list should contain the following
#students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)
students = ["Clark","Horan","Rai","White","Cooper","Jones","Cox","Smith"]

#b) use a method to order the students so that they are in alphabetical order (3 marks)
students.sort()

#17) create a tuple that represents exam marks with the following data. (4 marks)
#These are the respective exam marks for the alphabetically ordered student list
ExamMarks = [65,66,67,80,90,65,65,93] # 65,66,67,80,90,65,65,93
ExamMarks_tuple = tuple(ExamMarks) # Turns list into a tuple
print (ExamMarks_tuple)

#18) Dictionary question (9 marks)
#create a dictionary
#merging lists to dictionaries
ExanDictionary = dict(zip(students, ExamMarks_tuple))

#write code which adds both the student and a their corresponding mark. 
#do not perform this long hand (as in writing out the values above). Use data
print (ExanDictionary)#from the existing tuples above to create the dictionary

