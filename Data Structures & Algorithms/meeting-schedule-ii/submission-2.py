"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        free_times = []

        intervals.sort(key=lambda a: a.start)

        heapq.heappush(free_times, intervals[0].end)

        for i in range(1,len(intervals)):
            curr_start = intervals[i].start
            curr_end = intervals[i].end

            if curr_start >= free_times[0]:
                heapq.heappop(free_times)
            
            heapq.heappush(free_times, curr_end)
        
        return len(free_times)
