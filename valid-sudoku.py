# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according 
# to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for i in range(9)]
        cols = [set() for j in range(9)]
        boxes = [set() for k in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in rows[r]:
                    return False

                if num in cols[c]:
                    return False

                box = ((r //3) * 3) + (c // 3)

                if num in boxes[box]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True
        