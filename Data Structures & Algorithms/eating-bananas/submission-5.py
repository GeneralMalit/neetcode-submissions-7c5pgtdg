import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = 1
        while l <= r:
            m = (l + r) // 2
            time = sum(math.ceil(i/m) for i in piles)
            if time > h:
                l = m + 1
            else:
                speed = m
                r = m - 1
        return speed
