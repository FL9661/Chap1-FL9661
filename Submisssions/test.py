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