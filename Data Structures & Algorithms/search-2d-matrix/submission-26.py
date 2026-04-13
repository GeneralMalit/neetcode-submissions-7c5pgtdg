class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, (m * n) - 1
        while l <= r:
            i = (l + r) // 2
            val = matrix[i // n][i % n]
            print(f"val = {val}. l = {l}. r = {r}")
            if val < target:
                l = i + 1
            elif val > target:
                r = i - 1
            else:
                return True
        
        return False