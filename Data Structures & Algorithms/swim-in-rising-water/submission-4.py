import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    heapq.heappush(min_heap, (max(grid[nr][nc], t), nr, nc))

        return -1
