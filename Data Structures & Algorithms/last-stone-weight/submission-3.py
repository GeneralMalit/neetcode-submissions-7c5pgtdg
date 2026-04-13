import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)


        while len(heap) > 1:
            largest = heapq.heappop(heap)
            larger = heapq.heappop(heap)

            if largest != larger:
                heapq.heappush(heap, largest - larger)
            
        return -heap[0] if heap else 0