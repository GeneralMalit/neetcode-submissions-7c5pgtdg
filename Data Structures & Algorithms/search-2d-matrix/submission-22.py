class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0])) - 1 
        n = len(matrix[0])
        while l <= r:
            m = (l + r) // 2
            box = matrix[m// n][m % n]
            if box == target:
                return True
            elif box < target:
                l = m + 1
            else:
                r = m - 1
        return False