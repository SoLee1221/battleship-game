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
number_of_rounds = 10

"""
Create try function for incorrect input and correct input by user
col and row example none integer or str 
Also
Repeats invalid input until user inputs 
correct data to progress further in the game

"""
def guess_input():
    guess_row = input("guess_row: ")
    valid_input = True
    try:
        guess_row = int(guess_row)
        if guess_row > board_size or guess_row < 0:                    
            print("Invalid input")
            valid_input = False
    except ValueError:
        print("That's not a number")
        valid_input = False

    while not valid_input:
        guess_row = input("guess_row: ")
        valid_input = True
        try:
            guess_row = int(guess_row)
            if guess_row >= board_size or guess_row < 0:
                print("Invalid input")
                valid_input = False
        except ValueError:
            print("That's not a number")
            valid_input = False
    return guess_input   

def output_game():
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations you have sunk my ship!!!")
        #todo
    else:
        if board[guess_row][guess_col] == "x":
            print("You already guessed this one already!")
        else:
            print("You missed my ship!")
            board[guess_row][guess_col] = "x"
            whole_board(board)

def last_round():
    if number_of_rounds == last_round
    print("Game Over!!!")

for turn in range(number_of_rounds):
    print("Round", turn + 1)
    guess_row = guess_input()
    guess_col = guess_input()
    output_game()
    last_round()