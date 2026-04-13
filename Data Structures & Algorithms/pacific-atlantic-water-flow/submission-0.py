class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(visited)

            while q:
                r, c = q.popleft()

                for dr, dc in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
            return visited
        
        pacific_starts = [(0, c) for c in range(cols)] + [(r ,0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append((r, c))
        return res

