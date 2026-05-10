import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for x in stones:
            heapq.heappush(min_heap, -x)
        
        while len(min_heap) >= 2:
            x1, x2 = heapq.heappop(min_heap), heapq.heappop(min_heap)
            new = -x1 + x2
            if new > 0:
                heapq.heappush(min_heap, -new)

        if min_heap:
            return -min_heap[0]
        else:
            return 0