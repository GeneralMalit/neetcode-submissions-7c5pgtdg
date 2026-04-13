from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                char = board[r][c]
                if char == ".":
                    continue
                
                if char in rows[r] or char in cols[c] or char in box[(r//3, c//3)]:
                    return False
                
                rows[r].add(char)
                cols[c].add(char)
                box[(r//3, c//3)].add(char)
        
        return True
