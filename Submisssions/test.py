# Lab 3.4.1.6: the basics of lists #
# F Lyness
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