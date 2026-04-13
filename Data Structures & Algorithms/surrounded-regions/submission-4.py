class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()

        def dfs(r, c):
            print(f"r,c = {r}, {c}")
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1 , c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                print(f"r = {r}. c = {c}. {[0, rows -1 ]} {[0, cols - 1]} {board[r][c]} ")
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == "O":
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

                
