class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = []
        heights.append(0)
        for idx, val in enumerate(heights):
            while stk and heights[stk[-1]] > val:
                h = heights[stk.pop()]
                l = idx if not stk else idx - stk[-1] -1
                res = max(res, h * l)
            stk.append(idx)
        return res