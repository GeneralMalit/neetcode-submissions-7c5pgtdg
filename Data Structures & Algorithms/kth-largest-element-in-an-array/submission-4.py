import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            val = i
            if len(heap) < k:
                heapq.heappush(heap, val)
            elif heap[0] < val:
                heapq.heapreplace(heap, val)

        return  heap[0]

