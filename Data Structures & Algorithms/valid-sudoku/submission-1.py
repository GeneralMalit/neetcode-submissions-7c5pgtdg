from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]

                if val == ".":
                    continue
                box_key = (r // 3, c // 3)
                if(val in rows[r] or val in cols[c] or val in box[box_key]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                box[box_key].add(val)
        
        return True
