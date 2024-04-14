class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for curr_len in range(2,n+1):
            for i in range(0, n-curr_len+1):
                j = curr_len + i -1

                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        mid = n//2

        for i in range(0,n):
            for j in range(0,mid):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp
            