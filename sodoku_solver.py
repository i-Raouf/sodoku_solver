# 0 --> empty cell
puzzle = [
    [0, 0, 0,   2, 0, 0,   0, 0, 5],
    [3, 9, 0,   0, 5, 0,   0, 0, 0],
    [0, 0, 0,   7, 1, 9,   0, 8, 0],
     
    [0, 5, 0,   0, 6, 8,   0, 0, 0],
    [2, 0, 6,   0, 0, 3,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 4],
     
    [5, 0, 0,   0, 0, 0,   0, 0, 0],
    [6, 7, 0,   0, 0, 5,   0, 4, 0],
    [1, 0, 9,   0, 0, 0,   2, 0, 0],
]

def find_next_empty(puzzle):
    # return row, col or None, None (if no empty cell)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start,row_start +3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sodoku(puzzle):
    # choose a cell
    row, col = find_next_empty(puzzle)

    # all cells visited
    if row is None:
        return True

    # pick a number (1-9)
    for guess in range(1,10):
        # check valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recursive call
            if solve_sodoku(puzzle):
                return True

        # not valid guess or puzzle not solved --> backtrack
        puzzle[row][col] = 0 # reset cell

    # no solution found
    return False

if __name__ == "__main__":
    print(solve_sodoku(puzzle))
    for r in range(9):
        print(" ".join([str(i) for i in puzzle[r]]))