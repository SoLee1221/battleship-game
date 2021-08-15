from random import randint

board = []

board_size = 6

for i in range(board_size):
    board.append(["0"] * board_size)

def whole_board(board):
    for i in board:
        print(" ".join(i))

whole_board(board)

def random_row(board):
    return randint(0, len(board) -1)

def random_col(board):
    return randint(0, len(board[0]) -1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

"""
Create try function for incorrect input and correct input by user
col and row example none integer or str
"""
def guess_input(row):
    guess_row = input("guess_row: ")
    valid_input = True
    try:
        guess_row = int(guess_row)
    if guess_row >= board_size or guess_row < 0:
        print("Invalid input")
        valid_input = False
    except ValueError:
        print("That's not a valid input!")
        valid_input = False
"""
Repeats invalid input until user inputs 
correct data to progress further in the game
"""
    while not valid_input:
        guess_row = input("guess_row: ")
        valid_input = True
        try:
            guess_row = int(guess_row)
            if guess_row >= board_size or guess_row < 0:
                print("Invalid input")
                valid_input = False
        except ValueError:
            print("That's not a valid input!")
            valid_input = False
    return guess_row
    

def output_game():
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations you have sunk my ship!!!")
        break
    else:
        if guess_row >= board_size or guess_col >= board_size or guess_row < 0 or guess_col < 0:
            print("Oops thats not in the ocean range please try again!")
        elif board[guess_row][guess_col] == "x":
            print("You already guessed this one already!")
        else:
            print("You missed my ship!")
            board[guess_row][guess_col] = "x"
            if turn == 9:
                print("Game Over!!")
            whole_board(board)