def print_board(board):
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))         #print board template
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t     |     |")

def box_check(board, row, column):
    if row not in range(0,3) or column not in range(0,3):       #check if player chose place inside the board
        print('Error, please choose correct place on the board')#range is 0-3 because we don't tell player 0-2, instead is 1-3 for him
        return False
    else:
        if board[row][column] == '-':                           #if the place is empty ('-') - return true to continue
            return True
        else:
            print('The chosen place is not empty, please choose again')     #the place is inside the board but not empty, return false for new iteration
            return False

def receive_input_row():
    row = int(input('Please enter desired row: '))  #function to receive row input
    return row
def receive_input_column():
    column = int(input('Please enter desired column: '))        #function to receive column input
    return column

def victory_check(board):
    if board[0][0] == board[1][1] == board[2][2] != '-':            #victory check for diagonals
        return True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True                                                 #return true if any victory condition met
    for col in range(0,3):
        if board[0][col] == board[1][col] == board[2][col] != '-':  #check for columns
            return True
    for row in range(0,3):
        if board[row][0] == board[row][1] == board[row][2] != '-':  #check for rows
            return True

def board_full(board):
    count = 0
    for row in board:           #check if the board is full in for running on the rows (3 times) counting '-' (empty spaces)
        count += row.count('-')
    if count == 0:              #return count of 0 if no empty spaces left
        return count

def new_game():
    decision = input('Another game? (Type y for new game, any other symbol to exit) ') #receive input of symbol for new game of exit
    if decision.lower() == 'y':
        global board
        board = [['-','-','-'],['-','-','-'],['-','-','-']]         #global board new initialization
    else:
        return exit('Thanks for playing!')                          #if other symbol than Y entetred - exit the program

board = [['-','-','-'],['-','-','-'],['-','-','-']];    #initial board initialization

print('Welcome to the game!')
print_board(board)                      #First board print at the start + setting turn to X player
current_player_symbol = 'X'

while True:

    row = receive_input_row() - 1           #using -1 so the player can type normal numbers for row and column
    column = receive_input_column() - 1     #ex. 3 instead of 2 and 1 instead of 0

    if(box_check(board, row, column)) == False:     #check if input is inside the board and not taken
        continue                                    #if function return false -> go to next iteration with calling of input funcs again
    else:
        board[row][column] = current_player_symbol  #insert player symbol to board
        print_board(board)                          #print the new board after the change

        if board[row][column] == 'O':               #condition to change symbol (another player turn)
            if victory_check(board):                #if true returned - print the winner and propose new game
                print(f'Player {current_player_symbol} win!')
                new_game()
                continue
            current_player_symbol = 'X'             #if we entered X during the turn, next symbol would be O and vice versa
        else:
            if victory_check(board):                #if true returned - print the winner and propose new game
                print(f'Player {current_player_symbol} win!')
                new_game()
                continue
            current_player_symbol = 'O'             #same as X, setting the next player turn

        print('Next player turn!')

    if board_full(board) == 0:                      #check for draw at the end of turn
        print('The board is full, it is a draw!')
        new_game()
