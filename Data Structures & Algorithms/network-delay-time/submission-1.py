from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_heap = [(0, k)]
        visited = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            
            visited[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        if len(visited) == n:
            return max(visited.values())
        else:
            return -1