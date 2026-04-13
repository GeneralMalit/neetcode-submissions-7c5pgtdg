class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        n = len(matrix[0])

        while l <= r:
            m = (l + r) // 2
            print(f"matrix{m//n}, {m%n}. given {m}")
            block = matrix[m // n][m % n]
            if block == target:
                return True
            elif block > target:
                r = m - 1
            else:
                l = m + 1

        return False