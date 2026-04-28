class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1
        while l <= r:
            m = (l + r) // 2
            curr = matrix[m // cols][m % cols]
            if curr == target:
                return True
            elif curr > target:
                r = m - 1
            else:
                l = m + 1
        return False