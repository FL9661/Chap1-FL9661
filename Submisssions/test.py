newbeatles = ('ss')
for elements in newbeatles:
   
    while True:
        userinput1 = input('Which band member had intials that where SS? ')
        if  userinput1 != newbeatles:
            print ('try again:', '\n')
        elif userinput1 == newbeatles:
            print ('correct')
            break
        else:
             print ('close') 
             end()