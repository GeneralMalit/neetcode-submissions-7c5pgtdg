import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for i in stones:
            heapq.heappush(min_heap, -i)
        
        while len(min_heap) > 1:
            x1, x2 = heapq.heappop(min_heap), heapq.heappop(min_heap)
            total = -x1 + x2
            if total != 0:
                heapq.heappush(min_heap, -total)
            
        if min_heap:
            return -1 *min_heap[0]
        else:
            return 0