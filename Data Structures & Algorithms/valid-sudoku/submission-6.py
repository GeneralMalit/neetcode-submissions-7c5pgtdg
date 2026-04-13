from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        box = collections.defaultdict(list)

        r, c = len(board), len(board[0])

        for i in range(r):
            for j in range(c):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i] or val in cols[j] or val in box[(i // 3, j // 3)]:
                    return False
                rows[i].append(val)
                cols[j].append(val)
                box[(i//3, j//3)].append(val)
        return True