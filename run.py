from random import randint

player_board = []
ai_board = []

board_size = 6

def init_board(board):
    for i in range(board_size):
        board.append([empty_char] * board_size)

def whole_board(player_board):
    for i in player_board:
        print(" ".join(i))

whole_board(player_board)

def random_row(player_board):
    return randint(0, len(player_board) -1)

def random_col(player_board):
    return randint(0, len(player_board[0]) -1)

ship_row = random_row(player_board)
ship_col = random_col(player_board)
print(ship_row)
print(ship_col)
number_of_rounds = 10
empty_char = "."
miss_char = "0"
ship_char = "I"
hit_char = "X"

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

def fire(guess_row, guess_col, board):
    if board[guess_row][guess_col] == empty_char:
        board[guess_row][guess_col] = miss_char
        print("You missed!")
    elif board[guess_row][guess_col] == hit_char:
        print("You already guessed this one already!")
    elif board[guess_row][guess_col] == ship_char:
        board[guess_row][guess_col] = hit_char
        print("You sunk my ship!")
    elif board[guess_row][guess_col] == miss_char:
        print("You missed my ship!")


def player_turn():
    guess_row = guess_input()
    guess_col = guess_input()
    fire(guess_row, guess_col, ai_board)

def ai_turn():
    guess_row = guess_input()
    guess_col = guess_input()
    fire(guess_row, guess_col, player_board)

init_board(player_board)
init_board(ai_board)

for turn in range(number_of_rounds):
    player_turn()
    if is_dead(ai_board):
        print("You win!")
        break
    ai_turn()
    if is_dead(player_board):
        print("You loose!")
        break
    print("Round", turn + 1)
    output_game(turn == number_of_rounds -1)