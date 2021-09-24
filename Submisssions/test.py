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