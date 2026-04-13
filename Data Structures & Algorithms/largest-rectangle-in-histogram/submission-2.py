class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area