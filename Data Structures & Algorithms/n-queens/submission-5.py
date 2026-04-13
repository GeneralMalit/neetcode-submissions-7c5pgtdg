class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_dia = set()
        neg_dia = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(r) for r in board])
                return

            for c in range(n):
                if c in cols or (r - c) in neg_dia or (r + c) in pos_dia:
                    continue

                cols.add(c)
                pos_dia.add(r + c)
                neg_dia.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                pos_dia.remove(r + c)
                neg_dia.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
        
