class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_dia = set()
        neg_dia = set()
        board = [["."] * n for _ in range(n)]
        res = []
        
        def backtrack(r):
            if r == n:
                res.append(["".join(i) for i in board])
                return
            
            for c in range(n):
                if (c in cols or (r + c) in pos_dia or (r - c) in neg_dia):
                    continue

                board[r][c] = "Q"
                cols.add(c)
                pos_dia.add((r + c))
                neg_dia.add((r - c))

                backtrack(r + 1)
                board[r][c] = "."
                cols.remove(c)
                pos_dia.remove((r + c))
                neg_dia.remove((r - c))
                            
        backtrack(0)
        print(f"res = {res}")
        return res