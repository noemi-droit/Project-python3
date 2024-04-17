
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]

currentPlayer = "X"
winner= None
gameRunning= True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")
    

#Take player input
def playerInput (input):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
       board [inp-1] = currentPlayer
    else:
        print("Ooops chose another spot!")
    #Check your win or tie
#Switch the player
#Check for win or tie again
