from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        box = collections.defaultdict(list)
        n = len(board)
        for r in range(n):
            for c in range(n):
                char = board[r][c]

                if char == ".":
                    continue

                if char in row[r] or char in cols[c] or char in box[(r // 3, c // 3)]:
                    return False
                
                row[r].append(char)
                cols[c].append(char)
                box[(r // 3, c // 3)].append(char)

        return True