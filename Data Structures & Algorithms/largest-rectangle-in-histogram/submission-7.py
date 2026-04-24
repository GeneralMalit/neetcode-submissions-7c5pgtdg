class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk = []
        area = 0
        for idx, val in enumerate(heights):
            while stk and heights[stk[-1]] > val:
                h = heights[stk.pop()]
                w = idx if not stk else idx - stk[-1] - 1
                area = max(area, h * w)
            stk.append(idx)
        return area