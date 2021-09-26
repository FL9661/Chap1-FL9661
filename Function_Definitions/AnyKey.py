def Function_AnyKey():
    import msvcrt
    char = 0
    print ('Press the "Any" Key to continue...')
    while not char:
        char = msvcrt.getch()
        

print("Before Any Key")

Function_AnyKey()

print("After Anykey")
