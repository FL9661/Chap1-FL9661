# 3.1.2.3 Lab - while loops

secret_number = 777 # answer stored as a var

print('+================================+', '| Welcome to my game, muggle!    |', '| Enter an integer number        |', sep='\n')
print ('| and guess what number I\'ve     |', '| picked for you.                |', '| So, what is the secret number? |', sep='\n')
print ('+================================+')
#3 print lines used for welcome message.
guess = int(input('Input the correct Int No or become stuck in a loop forever: '))# will ask the user to enter an integer number for compairing with secret_answer later
while guess != secret_number: # statemenet identifies incorrect guess and prints line 11
    guess = int(input('Ha ha! You\'re stuck in my loop! Try again: '))
else:
    if guess == secret_number: # guess must match secret _number to print line 14
        print ('"Well done, muggle! You are free now."')

# 3.2.1.6 Lab - using for loop in a range with time delay to count to 5

import time
for i in range (1 , 6): # Write a for loop that counts to five.
    print(i, 'mississippi') # Body of the loop - print the loop iteration number and the word "Mississippi".
    use: time.sleep(1) # Body of the loop - use: time.sleep(1) - creates a time delay

print ('"Ready or not, here I come!"')# Writes a print function with the final message.

# 3.2.1.9 Lab - Using a break Loop Control

secret_word = 'chupacabra'
guess = input('Please guess the secret word: ') # users input of there guess word.
while True:
    if guess != secret_word: # If guess is not equal to secret_word - rechallenge user
        guess = input('Please guess the secret word: ') # rechallenge user
    if  guess == secret_word: # If guess is equal to secret_word
          break # exit loop then start at next print function
print ('You\'ve successfully left the loop.')

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

### 3.2.1.14 - building pyramid blocks  ###

blocks = int(input('Enter the number of blocks: '))

height = 0 # Light Blub var
in_row = 1 # Light Blub var, initial row is never below 1 but blocks can be zero
while in_row <= blocks: # Light Blub var = is the row number less or equal to blocks
    height += 1 # is less than blocks - add 1 to height
    blocks -= in_row # now reduce blocks by initial row value
    in_row +=1 # increase in_row value for next loop 
print('The height of the pyramid:', height) # prints hieght
# to print length insert "print ('The height of the pyramid:', (in_row - 1))""
