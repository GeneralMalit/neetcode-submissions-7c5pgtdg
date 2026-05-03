class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return False
        
        dp = {}
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            best = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            dp[(r, c)] = best
            return best
        return max(dfs(r, c) for r in range(rows) for c in range(cols))