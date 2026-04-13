from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = deque()
        fresh = 0 
        time = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rot.append((r, c))

        spread = [[-1,0],[1,0],[0,-1],[0,1]]

        while rot and fresh > 0:
            time += 1
            for i in range(len(rot)):
                x,y = rot.popleft()
                for dx, dy in spread:
                    newx, newy = x + dx, y + dy
                    print(f"cols = {cols}, rows = {rows}. newx newy = {newx}. {newy}")
                    if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        fresh -= 1
                        rot.append((newx, newy))

        return time if fresh == 0 else -1