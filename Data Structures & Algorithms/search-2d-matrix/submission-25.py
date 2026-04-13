class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        o = m * n 

        l, r = 0, o - 1
        
        while l <= r:
            mid = (l + r) // 2
            print(f"mid = {mid}, m = {m}")
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
