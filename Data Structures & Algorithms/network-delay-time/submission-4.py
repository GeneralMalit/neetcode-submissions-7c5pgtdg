from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        min_heap = [(0, k)]
        visited = {}

        while min_heap:
            time, u = heapq.heappop(min_heap)

            if u in visited:
                continue
            visited[u] = time

            for v, t in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (time + t, v))
        
        if len(visited) == n:
            return max(visited.values())
        else:
            return -1
