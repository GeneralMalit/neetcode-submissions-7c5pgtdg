from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                char = board[r][c]
                if char == ".":
                    continue
                if char in row[r] or char in col[c] or char in box[(r//3,c//3)]:
                    return False
                
                row[r].add(char)
                col[c].add(char)
                box[((r//3,c//3))].add(char)
        return True