"""
Project Euler 96: SuDoku

This is a sudoku solver using a backtracking approach.

Data Structures:
    empty_positions: 
      A stack containing the coordinates of currently empty positions.  Poping
      from this stack gives the next position to be filled in sequence.
    filled_positions: 
      A stack containing the currently filled positions.  Poping from this
      stack gives the most recently filled position.
"""

def read_all_puzzles(f):
    puzzles = []
    while True:
        header = f.readline()  # Skip lines like "Puzzle n"
        if header == "":
            break
        puzzles.append(read_one_puzzle(f))
    return puzzles

def read_one_puzzle(f):
    """Read one puzzle from an open file object."""
    puzzle = []
    for _ in range(9):
        row = list(f.readline().strip())
        puzzle.append(list(map(int, row)))
    return puzzle

def solve_puzzle(puzzle):
    empty_positions = build_empty_positions(puzzle)
    filled_positions = []
    working_puzzle = puzzle.copy()
    while empty_positions != []:
        current_position, current_n = empty_positions.pop()
        n = try_to_fill_position(current_position, current_n, working_puzzle)
        if n:
            filled_positions.append((current_position, n))
            working_puzzle[current_position[0]][current_position[1]] = n
        else:
            empty_positions.append((current_position, 0))
            working_puzzle[current_position[0]][current_position[1]] = 0
            empty_positions.append(filled_positions.pop())
    return working_puzzle 

def build_empty_positions(puzzle):
    empty_positions = []
    for i in range(8, -1, -1):
        row = puzzle[i]
        for j in range(8, -1, -1):
            n = row[j]
            if n == 0:
                empty_positions.append(((i, j), 0))
    return empty_positions

def try_to_fill_position(current_position, current_n, puzzle):
    for n in range(current_n + 1, 10):
        if (check_row(current_position, n, puzzle) and
            check_column(current_position, n, puzzle) and
            check_box(current_position, n, puzzle)):
            return n
    return None

def check_row(current_position, current_n, puzzle):
    row = puzzle[current_position[0]]
    return current_n not in row

def check_column(current_position, current_n, puzzle):
    column = set(puzzle[i][current_position[1]] for i in range(9))
    return current_n not in column 

def check_box(current_position, current_n, puzzle):
    b_row, b_col = current_position[0] // 3, current_position[1] // 3
    box = set(puzzle[i][j] for i in range(3*b_row, 3*b_row + 3)
                           for j in range(3*b_col, 3*b_col + 3))
    return current_n not in box


if __name__ == '__main__':
    f = open('data/sudoku-puzzles.txt')
    puzzles = read_all_puzzles(f)
    solved_puzzles = [solve_puzzle(puzzle) for puzzle in puzzles]

    # Compute the answer statistic
    s = 0
    for puzzle in solved_puzzles:
        row = puzzle[0]
        s += row[0]*100 + row[1]*10 + row[2]
    print(s)
