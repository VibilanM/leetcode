from collections import Counter

class Solution(object):
    def isValidSudoku(self, board):
        for i in board:
            c = Counter(i)
            del c['.']
            if c.values() != []:
                if max(c.values()) != 1:
                    return False

        cols = [[] for _ in range(9)]
        for j in board:
            for k in range(9):
                cols[k].append(j[k])
        
        for x in cols:
            d = Counter(x)
            del d['.']
            if d.values() != []:
                if max(d.values()) != 1:
                    return False
        
        threes = [[] for _ in range(9)]
        for y in range(9):
            for z in range(9):
                box_index = (y // 3) * 3 + (z // 3)
                threes[box_index].append(board[y][z])

        for a in threes:
            e = Counter(a)
            del e['.']
            if e.values() != []:
                if max(e.values()) != 1:
                    return False

        return True