import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, idx) for idx, q in enumerate(queries)], key=lambda x: x[0])
        i = 0
        res = [-1] * len(queries)
        min_heap = []
        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap:
                res[idx] = min_heap[0][0]
        return res