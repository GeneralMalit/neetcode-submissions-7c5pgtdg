from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        heap = [-val for val in counts.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                if val != 0:
                    q.append([val, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q[0][0])
                q.popleft()
        return time