from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_heap = [(0, k)]
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        visited = {}
        while min_heap:
            time, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited[u] = time
            
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (time + w, v))


        if len(visited) == n:
            return max(visited.values())
        else:
            return -1