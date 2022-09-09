win_cases = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
numbers_of_cells = {1: {1: 0, 2: 1, 3: 2}, 2: {1: 3, 2: 4, 3: 5}, 3: {1: 6, 2: 7, 3: 8}}


def print_board():
    print("---------")
    for row in board:
        print("| " + " ".join(row) + " |")
    print("---------")


def check_coordinates(x, y):
    if type(x) != int or type(y) != int:
        raise Exception("You should enter numbers!")
    elif x not in range(1, 4) or y not in range(1, 4):
        raise Exception("Coordinates should be from 1 to 3!")


def is_won(moves):
    return any([all([win_move in moves for win_move in win_case]) for win_case in win_cases])


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
X_moves = set()
O_moves = set()
empty = set()
turn = "X"
print_board()
while True:
    try:
        x, y = [int(coordinates) for coordinates in input().split()]
        check_coordinates(x, y)
        if board[x - 1][y - 1] != " ":
            raise Exception("This cell is occupied! Choose another one!")
        board[x - 1][y - 1] = turn
        c = numbers_of_cells[x][y]
        if turn == "X":
            X_moves.add(c)
            current_moves = X_moves
        else:
            O_moves.add(c)
            current_moves = O_moves

        if is_won(current_moves):
            print_board()
            print(f"{turn} wins")
            break
        if len(X_moves) + len(O_moves) == 9:
            print_board()
            print("Draw")
            break
        turn = "X" if turn == "O" else "O"
        print_board()

    except Exception as e:
        print(e)
        continue

