import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, 0)]
        total = 0
        visited = set()
        n = len(points)
        while min_heap:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total += cost
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))
        return total