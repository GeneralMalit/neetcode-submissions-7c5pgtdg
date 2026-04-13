import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = float("inf")
        while l <= r:
            m = (l + r) // 2
            time = sum((math.ceil(i/m)) for i in piles)
            if time <= h:
                min_rate = min(min_rate, m)
                r = m - 1
            else:
                l = m + 1
        return min_rate if min_rate != float("inf") else -1
