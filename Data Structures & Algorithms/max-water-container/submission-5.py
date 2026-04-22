class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxh = 0
        while l < r:
            maxh = max(maxh, (r - l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxh