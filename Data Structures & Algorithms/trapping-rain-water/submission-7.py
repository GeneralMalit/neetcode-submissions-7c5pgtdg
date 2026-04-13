class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                if height[l] < maxl:
                    res += maxl - height[l]
                else:
                    maxl = height[l]
            else:
                r -= 1
                if height[r] < maxr:
                    res += maxr - height[r]
                else:
                    maxr = height[r]
        return res