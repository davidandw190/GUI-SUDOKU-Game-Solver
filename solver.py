from random import randint

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    """
    Solves the board using backtracking.
    Returns True if a solution exists, False otherwise.
    """

    find = find_empty(bo)

    # base case
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    """
    Checks if the number placement on the is valid.
    """
    # Checks row
    for j in range(9):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False

    # Checks column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checks box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    box_x_delimiter = box_x * 3
    box_y_delimiter = box_y * 3

    for i in range(box_y_delimiter, box_y_delimiter + 3):
        for j in range(box_x_delimiter, box_x_delimiter + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# Uncomment this if you feel like checking how the solver performs on
# a board in the terminal
# --------------------------------------------------------------------
# def print_board(bo):
#     for i in range(9):
#
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - - - ")
#
#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")
#
#             if j == 8:
#                 print(bo[i][j])
#             else:
#                 print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    Finds an empty cell in the Sudoku board and returns its location.
    """
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j  # row, col
    return None


def pick_board(bo):
    find = find_empty(bo)

    # base case
    if not find:
        return True
    else:
        row, col = find

    used = []
    n = randint(1, 10)
    while n not in used:
        if valid(bo, n, (row, col)):
            bo[row][col] = n
            if solve(bo):
                return True
            bo[row][col] = 0
            used.append(n)
        else:
            used.append(n)

def build_board(bo):
    """
    Builds the Sudoku board by filling in digits based on the rules.
    """
    for i in range(9):
        passed = [1, 2, 3, 4]
        for j in range(9):
            empty_chance = randint(1, 7)
            if empty_chance in passed:
                bo[i][j] = 0
            else:
                continue

def generate_board(bo):
    """
    Generates a Sudoku board with a unique solution.
    """
    pick_board(bo)
    build_board(bo)
    return bo

# Feel free to play around
# -------------------------------------------------------------------
# generate_board(default)
# print_board(default)
# solve(default)
# print()
# print_board(default)
