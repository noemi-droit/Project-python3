import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]

currentPlayer = "X"
winner= None
gameRunning= True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")

# take player input
def playerInput(board):
    while True: 
        inp =input("Select a spot 1-9: ")
        if int(inp) in range(1,9):
            break
        else:
            print("that input will be invalid")
            continue
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")

 # check for win or tie
def checkHorizontal(board):
     global winner
     if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
     elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
     elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
 # switch the player
 # check for win or tie again 

while gameRunning:
    printBoard(board)
    playerInput(board)

