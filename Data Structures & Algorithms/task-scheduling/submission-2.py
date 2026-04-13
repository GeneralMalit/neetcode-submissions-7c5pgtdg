import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                val = heapq.heappop(heap)
                val += 1
                if val != 0:
                    q.append([val, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q[0][0])
                q.popleft()

        return time
                    