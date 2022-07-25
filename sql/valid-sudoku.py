"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = {
            '0': [0,0],
            '1': [0,3],
            '2': [0,6],
            '3': [3,0],
            '4': [3,3],
            '5': [3,6],
            '6': [6,0],
            '7': [6,3],
            '8': [6,6]
        }

        def validate(ty, items):
            processed_items = []
            print(f'validating {ty} : {items}')
            for item in items:

                if item!="." and item in processed_items:
                    return True
                else:
                    processed_items.append(item)

        for i in range(len(board)):

            # i(th) row items
            row_items = board[i]

            # i(th) column items
            col_items = [row[i] for row in board]

            # ith grid items
            grid_items = [board[r][c] for c in range(grids[str(i)][1], grids[str(i)][1]+3) for r in range( grids[str(i)][0], grids[str(i)][0]+3)]

            # Validate
            if validate('row', row_items) or validate('col', col_items) or validate('grid', grid_items):
                return False

        return True
