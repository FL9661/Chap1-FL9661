
print('''Tic Tac Toe

Instructions - Please enter coords using the map below

Board Co-Ordinates

Row1 = 0,0 - 0,1, - 0,2
Row2 = 1,0 - 1,1, - 1,2
Row3 = 2,0 - 2,1, - 2,2

''')







TTTBoard = [['_' for i in range(3)] for j in range(3)] # create complete board

for i in range(3): print(TTTBoard[i]) #print complete board
print()

Player1 = 'Francis'
print('Player1 is ', Player1)

for i in range(3):
    if input('please enter coord:') == i:
        TTTBoard.append('O')

for i in range(3): print(TTTBoard[i]) #print complete board
print()