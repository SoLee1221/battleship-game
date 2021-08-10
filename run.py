from random import randint

board = []

for i in range(0, 5):
    board.append(["0"] *5)

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
guess_row = int(input("guess_row: "))
guess_col = int(input("guess_col: "))

print(ship_row)
print(ship_col)

if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations you have sunk my ship!!!")
else:
    print("You missed my ship!")
    board[guess_row][guess_col] = "x"
    whole_board(board)