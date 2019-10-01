import random
def drawboard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_letter():
    letter=' '
    while 1:
          print('You want X or you want O?')
          letter=input()
          if letter=='X' or letter =='O':
              break
    if letter=='X':
          return ['X','O']
    else:
          return ['O','X']
def playagain():
    print("Do you want to play again? Enter 'y' or 'Y' to play again")
    ch=input()
    if ch=='Y' or ch=='y':
        tic_tac_toe()
def makemove(board,letter,move):
    board[move]=letter
def checkwinner(board,letter):
    return ((board[7]==board[8]==board[9]==letter) or(board[4]==board[5]==board[6]==letter) or(board[1]==board[2]==board[3]==letter) or (board[7]==board[4]==board[1]==letter) or (board[8]==board[5]==board[2]==letter) or (board[9]==board[6]==board[3]==letter) or (board[7]==board[5]==board[3]==letter) or (board[9]==board[5]==board[1]==letter))  
def boardcopy(board):
    dboard=[]
    for i in board:
        dboard.append(i)
    return dboard
def ismovefree(board,move):
    if board[move]==' ':
        return True
    else:
        return False
def getplayermove(board):
    while 1:
        print('PLAY YOUR CHANCE')
        move=input()
        if move>=1 and move<=9 and ismovefree(board,move):
            break
        else:
            print("Invalid Move!")
    return int(move)
def comp_move(board,cletter):
    if cletter=='X':
        pletter='O'
    else:
        pletter='X'
    for i in range(1,10):
        copyboard=boardcopy(board)
        if ismovefree(copyboard,i):
            makemove(copyboard,cletter,i)
            if checkwinner(copyboard,cletter):
                return i
    for i in range(1,10):
        copyboard=boardcopy(board)
        if ismovefree(copyboard,i):
            makemove(copyboard,pletter,i)
            if checkwinner(copyboard,pletter):
                return i
    if ismovefree(board,5):
        return 5
    if ismovefree(board,1):
        return 1
    if ismovefree(board,3):
        return 3
    if ismovefree(board,7):
        return 7
    if ismovefree(board,9):
        return 9
    if ismovefree(board,2):
        return 2
    if ismovefree(board,4):
        return 4
    if ismovefree(board,6):
        return 6
    if ismovefree(board,8):
        return 8        
def boardfull(board):
    for i in range(1,10):
        if ismovefree(board,i):
            return False
    return True
def tic_tac_toe():
    print('Welcome to Tic Tac Toe!')
    board=[' ']*10
    pletter,cletter=player_letter()
    while 1:
        choice=input("Enter 0 if you want to play first and 1 if you want to play second : ")
        if choice==0:
            turn='player'
            break
        else:
            if choice==1:
                turn='computer'
                break
            else:
                print "Error Invalid choice! Try again!"
                continue
    print('The'+turn+'will play first!')
    flag=0
    while not flag:
        if turn =='player':
            drawboard(board)
            move=getplayermove(board)
            makemove(board,pletter,move)
            if checkwinner(board,pletter):
                drawboard(board)
                print("Congratulations! You have won the game!")
                flag=1
            else:
                if boardfull(board):
                    drawboard(board)
                    print("Oh! Its a tie!")
                    break
                else:
                    turn='computer'
        else:
            move=comp_move(board,cletter)
            makemove(board,cletter,move)
            if checkwinner(board,cletter):
                drawboard(board)
                print("Oops! Computer have won the game!")
                print("Better luck next time!")
                flag=1
            else:
                if boardfull(board):
                    drawboard(board)
                    print("Oh! Its a tie!")
                    break
                else:
                    turn='player'
    playagain()
