class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        remove = 0
        prev_end = intervals[0][1]

        for i in intervals[1:]:
            if i[0] < prev_end:
                remove += 1
            else:
                prev_end = i[1]
        return remove