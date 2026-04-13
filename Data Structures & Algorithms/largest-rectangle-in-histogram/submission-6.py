class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for idx, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                h = heights[stack.pop()]
                w = idx if not stack else idx - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(idx)
        return max_area