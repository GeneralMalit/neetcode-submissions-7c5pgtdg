from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
        min_heap = [(0, k)]
        visited_times = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited_times:
                continue
            
            visited_times[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in visited_times:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        if len(visited_times) == n:
            return max(visited_times.values())
        else:
            return -1