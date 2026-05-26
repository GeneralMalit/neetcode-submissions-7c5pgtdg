import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            x1, x2 = heapq.heappop(heap), heapq.heappop(heap)
            val = -(-x1 + x2)
            if val != 0:
                heapq.heappush(heap, val)
            

        return -1 * heap[0] if len(heap) > 0 else 0
            