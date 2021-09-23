# Lab 3.6.1.9 - copying uniques numbers to a new list # 

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