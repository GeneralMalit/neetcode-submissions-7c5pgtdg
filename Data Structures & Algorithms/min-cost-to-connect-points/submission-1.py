import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0
        n = len(points)
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost

            for v in range(n):
                if v not in visited:
                    dist = abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1])
                    heapq.heappush(min_heap, (dist, v))
        return total_cost