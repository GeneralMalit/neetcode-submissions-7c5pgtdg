class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m*n) - 1

        while l <= r:
            i = (l + r) // 2
            print(f"i = {i}, i // m = {i // m} and i % n = {i%n}")
            m_act = matrix[i // n][i % n]

            if m_act == target:
                return True
            elif m_act < target:
                l += 1
            else:
                r -= 1
        return False