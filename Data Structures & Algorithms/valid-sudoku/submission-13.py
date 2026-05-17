from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                if num in row[r] or num in col[c] or num in box[(r//3,c//3)]:
                    return False
                row[r].append(num)
                col[c].append(num)
                box[(r//3,c//3)].append(num)
        return True