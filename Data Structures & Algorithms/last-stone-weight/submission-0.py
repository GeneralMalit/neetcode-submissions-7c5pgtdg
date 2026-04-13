import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            biggest = heapq.heappop(heap)
            biggest2 = heapq.heappop(heap)

            if biggest != biggest2:
                heapq.heappush(heap, biggest - biggest2)

        return -heap[0] if heap else 0 

