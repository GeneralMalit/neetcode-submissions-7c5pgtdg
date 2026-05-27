from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-val for idx, val in Counter(tasks).items()]
        heapq.heapify(heap)
        time = 0
        q = deque()

        while q or heap:
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