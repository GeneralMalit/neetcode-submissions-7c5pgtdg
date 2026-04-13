import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []

        for i in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, i)
            elif minheap[0] < i:
                heapq.heapreplace(minheap, i)
        
        return minheap[0]