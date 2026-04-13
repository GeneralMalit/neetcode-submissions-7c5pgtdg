import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for i in stones:
            heapq.heappush(min_heap, -i)

        while len(min_heap) > 1:
            s1 = -1 * heapq.heappop(min_heap)
            s2 = -1 * heapq.heappop(min_heap)

            s3 = abs(s1 - s2)

            if s3 > 0:
                heapq.heappush(min_heap, -1 * s3)

        return 0 if len(min_heap) == 0 else -1 * min_heap[0]           


