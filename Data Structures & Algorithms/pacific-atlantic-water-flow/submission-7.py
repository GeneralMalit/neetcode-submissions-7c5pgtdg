from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (-1 ,0), (0, 1), (0, -1)]
        def bfs(starts):
            a = set(starts)
            b = deque(a)
            while b:
                for i in range(len(b)):
                    r, c = b.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in a and heights[nr][nc] >= heights[r][c]:
                            a.add((nr, nc))
                            b.append((nr, nc))

            return a
        
        pacific = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        pac, atl = bfs(pacific), bfs(atlantic)
        return list(pac.intersection(atl))