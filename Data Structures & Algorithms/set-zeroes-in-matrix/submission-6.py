class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        row1 = False
        for r in range(rows):
            if matrix[r][0] == 0:
                row1 = True
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
        
        if row1:
            for r in range(rows):
                matrix[r][0] = 0
