class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[0])):
                if j == 0:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j+1]) + matrix[i][j]
                elif j == len(matrix[0])-1:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j-1]) + matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j],min(matrix[i-1][j-1],matrix[i-1][j+1])) + matrix[i][j]
                
        #print(matrix)
        
        return min(matrix[len(matrix)-1])