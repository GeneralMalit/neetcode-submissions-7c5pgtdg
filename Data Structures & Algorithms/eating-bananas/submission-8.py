class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = 1
        while l <= r:
            m = (l + r) // 2

            total = sum((m + i - 1) // m for i in piles)
            if total > h:
                l = m + 1
            else:
                speed = m
                r = m - 1
        return speed