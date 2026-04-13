class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, grid):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            grid[r][c] = 0

            return 1 + (
                dfs(r - 1, c, grid) + 
                dfs(r + 1, c, grid) + 
                dfs(r, c - 1, grid) + 
                dfs(r, c + 1, grid)  
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c, grid))

        return maxArea