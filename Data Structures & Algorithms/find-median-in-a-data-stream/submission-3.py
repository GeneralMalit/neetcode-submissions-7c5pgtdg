import heapq
class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.large_half = []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half, -1 * num)

        if (self.small_half and self.large_half and self.small_half[0] * -1 > self.large_half[0]):
            val = -1 * heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)
        
        if len(self.small_half) > len(self.large_half) + 1:
            val = -1 * heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)
        
        if len(self.large_half) > len(self.small_half):
            val =  heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -1 * val)
            

    def findMedian(self) -> float:
        if len(self.small_half) > len(self.large_half):
            return -1 * self.small_half[0]
        else:
            return (-1 * self.small_half[0] + self.large_half[0]) / 2.0
        
        