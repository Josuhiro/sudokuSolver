#Sudoku Solver with backtracking algorithm
board = [
    [7, 0, 4, 5, 3, 0, 2, 0, 0],
    [0, 0, 8, 1, 6, 0, 0, 0, 0],
    [1, 0, 2, 0, 0, 0, 6, 8, 5],
    [0, 0, 7, 9, 1, 0, 0, 6, 8],
    [0, 0, 5, 0, 0, 7, 3, 0, 2],
    [6, 8, 0, 0, 5, 4, 1, 9, 0],
    [0, 0, 0, 7, 0, 0, 8, 0, 0],
    [2, 5, 0, 0, 0, 0, 4, 7, 3],
    [0, 0, 0, 0, 4, 0, 0, 2, 6],
]


def valid(board, number, position):
    # checking row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # checking column
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # checking square
    square_x = position[1] // 3
    square_y = position[0] // 3

    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True
            board[row][column] = 0
    return False


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


print("Starting sudoku:")
print_board(board)
solve(board)
print("* " * 12)
print("Solved sudoku:")
print_board(board)
