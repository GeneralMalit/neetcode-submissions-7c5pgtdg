from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        heap = [-val for val in Counter(tasks).values()]
        heapq.heapify(heap)

        time = 0

        while q or heap:
            time += 1
            if heap:
                curr = heapq.heappop(heap)
                curr += 1
                if curr != 0:
                    q.append([curr, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q[0][0])
                q.popleft()
                
        return time