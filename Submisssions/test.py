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