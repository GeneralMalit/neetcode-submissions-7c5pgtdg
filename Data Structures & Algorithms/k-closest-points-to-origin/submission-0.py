import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = -(x**2 + y ** 2)

            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif heap[0][0] < dist:
                heapq.heapreplace(heap, (dist, x, y))

        return [[x, y] for dist, x, y in heap]