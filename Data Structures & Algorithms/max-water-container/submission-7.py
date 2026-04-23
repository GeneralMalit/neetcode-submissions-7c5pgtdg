class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mw = 0
        l, r = 0, len(heights) - 1
        while l < r:
            mw = max(mw, (r - l) * min(heights[l], heights[r]))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return mw