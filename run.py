from random import randint

player_board = []
ai_board = []

board_size = 6

def init_board(board):
    for i in range(board_size):
        board.append([empty_char] * board_size)

def whole_board(board, hide_ships):
    for i in board:
        line = " ".join(i)
        if hide_ships == True:
            line = line.replace(ship_char, empty_char)
        print(line)

def guess_random():
    return randint(0, board_size -1)

number_of_rounds = 10
empty_char = "."
miss_char = "X"
ship_char = "@"
hit_char = "*"

"""
Create try function for incorrect input and correct input by user
col and row example none integer or str 
Also
Repeats invalid input until user inputs 
correct data to progress further in the game

"""

def guess_input(s):
    guess_row = input(f"Guess {s}: ")
    valid_input = True
    try:
        guess_row = int(guess_row)
        if guess_row >= board_size or guess_row < 0:                    
            print("Invalid input")
            valid_input = False
    except ValueError:
        print("That's not a number")
        valid_input = False
    while not valid_input:
        guess_row = input(f"Guess {s}: ")
        valid_input = True
        try:
            guess_row = int(guess_row)
            if guess_row >= board_size or guess_row < 0:
                print("Invalid input")
                valid_input = False
        except ValueError:
            print("That's not a number")
            valid_input = False
    return guess_row     
"""
Prints output for player and computer depending on input given
"""
def fire(guess_row, guess_col, board, c):
    if board[guess_row][guess_col] == empty_char:
        board[guess_row][guess_col] = miss_char
        print(f"{c} missed!")
        return True
    if board[guess_row][guess_col] == hit_char:
        print(f"{c} already guessed this one already!")
        return False
    if board[guess_row][guess_col] == ship_char:
        board[guess_row][guess_col] = hit_char
        print(f"{c} sunk my ship!")
        return True
    if board[guess_row][guess_col] == miss_char:
        print(f"{c} has already guessed this one already!")
        return False

def clear_input():
    loop = True
    while loop:
        print("Player's board: ")
        whole_board(player_board, False)
        clear_inp = input("Would you like to reset your ships position? yes/no: ")
        if "yes" == clear_inp:
            clear_board(player_board)
            place_ship(player_board)
        else:
            loop = False

def player_turn():
    guess_row = guess_input("row")
    guess_col = guess_input("col")
    return fire(guess_row, guess_col, ai_board, "player")

def ai_turn():
    guess_row = guess_random()
    guess_col = guess_random()
    return fire(guess_row, guess_col, player_board, "computer")

def place_ship(board):
    ships = 0
    while ships < 3:
        ship_row = guess_random()
        ship_col = guess_random()
        if board[ship_row][ship_col] != ship_char:
            board[ship_row][ship_col] = ship_char
            ships += 1

def clear_board(board):
    for row in range(board_size):
        for col in range(board_size):
            board[row][col] = empty_char

def is_dead(board):
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == ship_char:
                return False    
    print("All ships destroyed!")
    return True
         
init_board(player_board)
init_board(ai_board)

another_game = True
while another_game:
    place_ship(player_board)
    place_ship(ai_board)
    clear_input

place_ship(player_board)
place_ship(ai_board)
clear_input()

for turn in range(number_of_rounds):
    print("Round", turn + 1)
    print("Player's board: ")
    whole_board(player_board, False)
    print("Computer's board: ")
    whole_board(ai_board, True)
    valid_move = player_turn()
    while not valid_move:
        valid_move = player_turn()
    if is_dead(ai_board):
        print("You win!")
        break
    valid_move = ai_turn()
    while not valid_move:
        ai_turn()
    if is_dead(player_board):
        print("You loose!")
        break