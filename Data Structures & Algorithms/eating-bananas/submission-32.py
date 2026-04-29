import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rate = 0
        while l <= r:
            m = (l + r) // 2
            curr = sum([math.ceil(i/m) for i in piles])
            if curr <= h:
                rate = m
                r = m - 1
            else:
                l = m + 1
        return rate