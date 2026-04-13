from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        q = collections.deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                val = 1 + heapq.heappop(heap)
                if val != 0:
                    q.append([val, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time