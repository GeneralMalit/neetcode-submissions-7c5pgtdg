class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r] 
        res = 0
        while l < r:
            if height[l] > height[r]:
                r -= 1
                if height[r] > maxr:
                    maxr = height[r]
                else:
                    res += maxr - height[r]
            else:
                l += 1
                if height[l] > maxl:
                    maxl = height[l]
                else:
                    res += maxl - height[l]
        return res