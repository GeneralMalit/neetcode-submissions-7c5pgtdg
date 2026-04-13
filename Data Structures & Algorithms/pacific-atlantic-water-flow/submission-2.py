class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            a = set(starts)
            q = deque(a)

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in a and heights[nr][nc] >= heights[r][c]:
                            a.add((nr, nc))
                            q.append((nr, nc))                    

            return a

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pac = bfs(pacific)
        atl = bfs(atlantic)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res

