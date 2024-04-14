class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        row_zero_is_zero = False
        col_zero_is_zero = False

        for i in range(n):
            if matrix[0][i] == 0:
                row_zero_is_zero = True

        for i in range(m):
            if matrix[i][0] == 0:
                col_zero_is_zero = True

        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        for i in range(n):
            if row_zero_is_zero:
                matrix[0][i] = 0

        for i in range(m):
            if col_zero_is_zero:
                matrix[i][0] = 0
        
        return