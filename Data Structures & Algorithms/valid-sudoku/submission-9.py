from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        def valid(r, c):
            char = board[r][c]
            if char in row[r] or char in col[c] or char in box[(r//3, c//3)]:
                print(f"here.")
                return False
            
            row[r].append(char)
            col[c].append(char)
            box[(r//3, c//3)].append(char)
            return True


        for r in range(9):
            for c in range(9):
                if board[r][c] != "." and not valid(r, c):
                    print(f"char is {board[r][c]}, currently failing at:")
                    return False
        return True

