class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                if maxl > height[l]:
                    res += maxl - height[l]
                else:
                    maxl = height[l]

            else:
                r -= 1
                if maxr > height[r]:
                    res += maxr - height[r]
                else:
                    maxr = height[r]
        return res