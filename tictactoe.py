from IPython.display import clear_output

def display_board(board):
    clear_output()
    print ( board[7]+"|"+board[8]+"|"+board[9])
    print ( '-----')
    print ( board[4]+"|"+board[5]+"|"+board[6])
    print ( '-----')
    print ( board[1]+"|"+board[2]+"|"+board[3])
    
def player_input():
    marker = ''
    
    while not ( marker == 'X' or marker == 'O'):
        marker = input('Player 1 do you want to be X or O?').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board,marker,position):
    board[position] = marker
    
def win_check(board,mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[9] == board[6] == board[3] == mark))

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player2'
    else:
        return 'Player1'
    
def space_check(board, position):
    return board [ position ] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    else:
        return True
        
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose your next position (1-9):"))
    return position

def replay():
    play_again = str(input("Would you like to play again? Y or N?  ")).upper()
    return play_again == 'Y'


print('WELCEME TO TIC TAC TOE')


while True:
    
    #first reset to an empty board. In our functions board is a list
    theboard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    start_game = str(input('Would you like to start the game. Select Y or N: '))
    if start_game.upper() == 'Y':
        game_on = True
    else:
        game_on = False
        
        
    while game_on:
        if turn == 'Player1':
            
            #Player 1 Turn
            
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
            
            if win_check(theboard, player1_marker):
                display_board(theboard)
                print('Player1 has won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player2'
                    
        else:           
            #Player 2 Turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Player2 has won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player1'
    if not replay():
        break