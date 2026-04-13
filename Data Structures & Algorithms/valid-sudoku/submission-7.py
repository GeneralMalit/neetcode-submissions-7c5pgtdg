from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        box = collections.defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board)):
                char = board[r][c]

                if char == ".":
                    continue

                if char in rows[r] or char in cols[c] or char in box[(r // 3, c // 3)]:
                    return False
                
                rows[r].append(char)
                cols[c].append(char)
                box[(r // 3, c // 3)].append(char)

        return True
                
