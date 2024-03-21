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


# check if a player has won
def check_win(board, player):
    win_combinations = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
]
for combination in win_combinations:
    if all( cell == player for cell in combination):
       return True
       return False

# play game
def play_game():
    board = [""]*9
    player = "X"
    while True:
        print_board(board)
        move=int(input(f"Player{player}, enter your move (1-9):"))-1
        if board[move]=='':
            board[move]= player
        if check_win(board,player):
              print_board(board)
              print(f"Player{player}wins!")
              break
        if ''not in board:
                print_board(board)
                print("It's a tie!")
                break
                player="O" if player =="X" else "X"
        else:
                print("Invalid move, try again.")

