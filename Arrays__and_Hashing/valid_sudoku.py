'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''

def valid_sudoku(board: list[list[str]]) -> bool:
    hashset = set()

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
                
            # Create unique identifiers for row, column, and sub-box checks
            row_check = f"row {i} {board[i][j]}"
            col_check = f"col {j} {board[i][j]}"
            box_check = f"box {i//3}{j//3} {board[i][j]}"
                
            # Check if any of these identifiers already exist in the set
            if (row_check in hashset or
                col_check in hashset or
                box_check in hashset):
                return False
                
            # Add the identifiers to the set
            hashset.add(row_check)
            hashset.add(col_check)
            hashset.add(box_check)
        
    return True

'''
TC is O(9^2) and SC is O(9^2) as well worst case. In this program we do a unique approach with strings and
a set to verify our constraints are met in terms of uniqueness. If at any point as we are iterating through
our board and we see that a value at a specific row, column, or square is contained in our hashset,
it indicates that we do not have a valid sudoku thus false. If are able to iterate through the entire 
board without finding any dups, we have a valid board.
'''

