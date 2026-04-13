class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited
        
        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        print(f"pacific\n{pacific}\n\natlantic\n{atlantic}")
        pac_bfs = bfs(pacific)
        atl_bfs = bfs(atlantic)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_bfs and (r, c) in atl_bfs:
                    res.append((r, c))
        return res

            

