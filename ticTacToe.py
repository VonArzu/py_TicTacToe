board = [' ' for x in range (10)] # this should be the first line in the program
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
def insertLetter(letter, pos):
    board[pos] = letter
def spaceIsFree(pos) :
    return board [pos] == ' '
def printBoard(board0):
    #"board" is a list of 10 strings representing the board (ingore index 0)
    print('    |    | ')
    print('  ' + board [1]  +  '  |  '  + board [2]  + '  |   '  +  board[3])
    print('    |   |')
    print('-----------')
    print('    |   |')
    print('  ' + board [4]  +  '  |  '  +  board[5]  + '  |   '  +  board [6])
    print('    |   |')
    print('-----------')
    print('    |   |')
    print('  ' + board[7]   +   '  |  '  + board[8]  +  ' |  '   + board[9])
    print('    |   |')
def isWinner(bo, le) :
    # Given a board and a player's letter, this function returns True if th at player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo [7] == le and bo[8] == le and bo[9] == le) or # across the top)
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle 
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side 
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le) or # diagonal

    