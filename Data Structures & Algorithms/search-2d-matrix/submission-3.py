class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = len(matrix) * len(matrix[0]) - 1
        l, r = 0, i

        while l <= r:
            m = (l + r) // 2
            val = matrix[m // n][m % n]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return False