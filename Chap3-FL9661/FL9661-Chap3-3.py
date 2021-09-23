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

print('step 4:', beatles)
print("The Fab", len(beatles)) # testing list legth

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