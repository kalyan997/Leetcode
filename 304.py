class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        self.matrix = [[0]*n for i in range(m)]
        self.sum_matrix = [[0]*(n+1) for i in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                self.matrix[i-1][j-1] = matrix[i-1][j-1]
                curr_sum = self.sum_matrix[i-1][j]+self.sum_matrix[i][j-1]-self.sum_matrix[i-1][j-1] + self.matrix[i-1][j-1]
                self.sum_matrix[i][j] = curr_sum
        #print(self.matrix)
        #print(self.sum_matrix)
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2+1][col2+1]-self.sum_matrix[row2+1][col1]-self.sum_matrix[row1][col2+1]+self.sum_matrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)