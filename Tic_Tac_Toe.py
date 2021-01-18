def display_board(board):
    print ('\n' *100 )
    print (board[7]+ '|'+ board[8]+ '|'+ board[9])
    print ('-----')
    print (board[4]+ '|'+ board[5]+ '|'+ board[6])
    print ('-----')
    print (board[1]+ '|'+ board[2]+ '|'+ board[3])

def player_input():
    marker = ['X','O']
    
    while not (marker == 'X' or marker == 'O' or marker == 'x' or marker == 'o'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ['X', 'O']
    if marker == 'O':
        return ['O', 'X']

def place_marker(board, marker, position):
    position_available = [1,2,3,4,5,6,7,8,9]
    marker_available = ['X', 'O']
    while position in position_available and marker in marker_available:
        board[position] = marker    
        break

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    first_player = str(random.randint(1,2))
    print (f'Player {first_player} goes first')
    return first_player

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    i = 1
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    choice = 'Wrong'
    acceptable_range = [1,2,3,4,5,6,7,8,9]
    within_range = False
    available = False
    while choice.isdigit() == False or within_range == False or available == False:
        choice = input('Please choose your next position(1-9: bottom left is 1): ')
        
        if choice.isdigit() == False:
            print ('The choice must be a digit')
        
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print ('Your choice is out of range. Please select between 1-9')
                within_range = False
        if within_range == True:       
            if space_check(board,int(choice)) == False:
                print ('Your choice is not available')
                available = False
            if space_check(board,int(choice)) == True:
                available = True
                chosen_position = choice
    
    return int(choice)
                
def replay():
    choice = 'Wrong'
    
    while choice not in ['Yes', 'No', 'yes', 'no']:
        choice = input('Do you want to play again?: ')
        if choice not in ['Yes', 'No', 'yes', 'no']:
            print ('Sorry I do not recognize that, please type in Yes or No')
    if choice == 'Yes' or choice == 'yes':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    tic_tac_toe = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    play_game = 'ZZZ'
    
    while play_game not in ['Yes', 'No', 'Yes', 'No']:
        play_game = input('Ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == '1':
            
            display_board(tic_tac_toe)
            position = player_choice(tic_tac_toe)
            place_marker(tic_tac_toe, player1_marker, position)
            
            if win_check(tic_tac_toe, player1_marker):
                display_board(tic_tac_toe)
                print('Congrats! Player 1 has won the game')
                game_on = False
            else:
                if full_board_check(tic_tac_toe):
                    display_board(tic_tac_toe)
                    print('The game is a draw!')
                    break
                else:
                    turn = '2'
        else:
            display_board(tic_tac_toe)
            position = player_choice(tic_tac_toe)
            place_marker(tic_tac_toe, player2_marker, position)

            if win_check(tic_tac_toe, player2_marker):
                display_board(tic_tac_toe)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(tic_tac_toe):
                    display_board(tic_tac_toe)
                    print('The game is a draw!')
                    break
                else:
                    turn = '1'

    if not replay():
        break
