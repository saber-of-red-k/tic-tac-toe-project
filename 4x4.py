import random, time

def print_board(board):
    print('\t     |     |     |')
    print('\t  {}  |  {}  |  {}  |  {}  '.format(board[0][0], board[0][1], board[0][2], board[0][3]))
    print('\t_____|_____|_____|_____')

    print('\t     |     |     |')
    print('\t  {}  |  {}  |  {}  |  {}  '.format(board[1][0], board[1][1], board[1][2], board[1][3]))         #print board template
    print('\t_____|_____|_____|_____')

    print('\t     |     |     |')
    print('\t  {}  |  {}  |  {}  |  {}  '.format(board[2][0], board[2][1], board[2][2], board[2][3]))
    print('\t_____|_____|_____|_____')

    print('\t     |     |     |')
    print('\t  {}  |  {}  |  {}  |  {}  '.format(board[3][0], board[3][1], board[3][2], board[3][3]))
    print('\t     |     |     |')

def box_check(board, row, column):
    if row not in range(0,4) or column not in range(0,4):       #check if player chose place inside the board
        print('Error, please choose correct place on the board')#range is 0-3 because we don't tell player 0-2, instead is 1-3 for him
        return False
    else:
        if board[row][column] == '-':                           #if the place is empty ('-') - return true to continue
            return True
        else:
            print('The chosen place is not empty, please choose again')     #the place is inside the board but not empty, return false for new iteration
            if mode == '2pc':
                time.sleep(0.2)                                             #if in 2pc mode - delay the console output so we can see it better
            return False

def receive_input_row():
    while True:                                                 #check that number entered and not symbol or enter (etgar1)
        inp = input('Please enter desired row: ')
        if inp == '1' or inp == '2' or inp == '3' or inp == '4':
            row = int(inp)
            return row
        else: continue
def receive_input_column():
    while True:
        inp = input('Please enter desired column: ')
        if inp == '1' or inp == '2' or inp == '3' or inp == '4':              #same as row check
            column = int(inp)
            return column
        else: continue

def victory_check(board):
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] != '-':            #victory check for diagonals
        return True
    if board[0][3] == board[1][2] == board[2][1] == board[3][0] != '-':
        return True                                                 #return true if any victory condition met
    for col in range(0,4):
        if board[0][col] == board[1][col] == board[2][col] == board[3][col] != '-':  #check for columns
            return True
    for row in range(0,4):
        if board[row][0] == board[row][1] == board[row][2] == board[row][3] != '-':  #check for rows
            return True

def next_turn_win(board,operator):              #board + operator (X or O)
    for lstIdx, lst in enumerate(board):
        if lst.count(operator) == 3:             #check to see if 2 elements match in rows
            index = lstIdx                                          #if yes - save index of row
            for idx, item in enumerate(lst):
                if board[lstIdx][idx] == '-':                       #check the position of empty space
                    print(f'Next turn win if you choose row {index + 1}, column {idx + 1}')     #print index of row + column of empty space

    reversed_board = list(zip(*board))                              #reverse the board to check for columns

    for lstIdx, lst in enumerate(reversed_board):                   #same check
        if lst.count(operator) == 3:
            index = lstIdx
            for idx, item in enumerate(lst):
                if reversed_board[lstIdx][idx] == '-':
                    print(f'Next turn win if you choose row {idx + 1}, column {index + 1}')         #row and column swapped

    if board[0][0] == board[1][1] == board[2][2] == operator:
        print(f'Next turn win if you choose row {3 + 1}, column {3 + 1}')
    elif board[0][0] == board[1][1] == board[3][3] == operator:
        print(f'Next turn win if you choose row {2 + 1}, column {2 + 1}')                           #diagonals check 1
    elif board[0][0] == board[2][2] == board[3][3] == operator:
        print(f'Next turn win if you choose row {1 + 1}, column {1 + 1}')
    elif board[1][1] == board[2][2] == board[3][3] == operator:
        print(f'Next turn win if you choose row {0 + 1}, column {0 + 1}')

    if board[0][3] == board[1][2] == board[2][1] == operator:
        print(f'Next turn win if you choose row {3 + 1}, column {0 + 1}')
    elif board[0][3] == board[1][2] == board[3][0] == operator:
        print(f'Next turn win if you choose row {2 + 1}, column {1 + 1}')                           #diagonals check 2
    elif board[0][3] == board[2][1] == board[3][0] == operator:
        print(f'Next turn win if you choose row {1 + 1}, column {2 + 1}')
    elif board[1][2] == board[2][1] == board[3][0] == operator:
        print(f'Next turn win if you choose row {0 + 1}, column {3 + 1}')

def board_full(board):
    count = 0
    for row in board:           #check if the board is full in for running on the rows (3 times) counting '-' (empty spaces)
        count += row.count('-')
    if count == 0:              #return count of 0 if no empty spaces left
        return count



def new_game():
    decision = input('Start new game? (Type y for new game, any other symbol to exit) ') #receive input of symbol for new game of exit
    if decision.lower() == 'y':
        global board
        board = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]         #global board new initialization
        global mode
        while True:
            mode = input('Which mode we are playing? (pc for vs computer, player for vs human, 2pc to watch two comps playing, other symbol to exit): ')
            if mode.lower() != 'pc' and mode.lower() != 'player' and mode.lower() != '2pc':
                continue
            else: return
    else:
        return exit('Thanks for playing!')                          #if other symbol than Y entetred - exit the program

board = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']];    #initial board initialization

print('Welcome to the game!')

new_game()                              #game start

print_board(board)                      #First board print at the start + setting turn to X player
print('\n')                             #To be a little bit prettier
current_player_symbol = 'X'

while True:
    if mode == 'pc':

        if current_player_symbol == 'X':
            row = receive_input_row() - 1           #using -1 so the player can type normal numbers for row and column
            column = receive_input_column() - 1     #ex. 3 instead of 2 and 1 instead of 0
        else:
            row = random.randint(0, 3)              #if we are in pc mode, instead of input we choose random numbers until it hits empty space
            column = random.randint(0, 3)

    elif mode == '2pc':
        row = random.randint(0,3)                   #in 2pc mode we go full random
        column = random.randint(0, 3)
    else:
        row = receive_input_row() - 1  # using -1 so the player can type normal numbers for row and column
        column = receive_input_column() - 1  # ex. 3 instead of 2 and 1 instead of 0

    if(box_check(board, row, column)) == False:     #check if input is inside the board and not taken
        continue                                    #if function return false -> go to next iteration with calling of input funcs again
    else:
        board[row][column] = current_player_symbol  #insert player symbol to board
        print_board(board)                          #print the new board after the change

        if mode == '2pc':                           #if in 2pc mode - delay the board print and the while loop so we can see it
            time.sleep(0.5)

        if board[row][column] == 'O':               #condition to change symbol (another player turn)
            if victory_check(board):                #if true returned - print the winner and propose new game
                print(f'Player {current_player_symbol} win!')
                new_game()
                continue
            next_turn_win(board, current_player_symbol)     #next turn win check
            current_player_symbol = 'X'             #if we entered X during the turn, next symbol would be O and vice versa
        else:
            if victory_check(board):                #if true returned - print the winner and propose new game
                print(f'Player {current_player_symbol} win!')
                new_game()
                continue
            next_turn_win(board,current_player_symbol)      #next turn win check
            current_player_symbol = 'O'             #same as X, setting the next player turn

        print('Next player turn!')

    if board_full(board) == 0:                      #check for draw at the end of turn
        print('The board is full, it is a draw!')
        new_game()
