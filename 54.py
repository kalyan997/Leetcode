class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        m = len(matrix)
        n = len(matrix[0])

        def isValidCoor(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True

        curr_dir = 0
        chng_dir = 0
        i = 0
        j = 0
        res.append(matrix[i][j])
        matrix[i][j] = 101
       

        while chng_dir < 2:
            while isValidCoor(i+directions[curr_dir][0], j+directions[curr_dir][1]) and matrix[i+directions[curr_dir][0]][j+directions[curr_dir][1]] != 101:
                chng_dir = 0
                i, j = i+directions[curr_dir][0], j+directions[curr_dir][1]
                res.append(matrix[i][j])
                matrix[i][j] = 101
                
            curr_dir = (curr_dir+1)%4
            chng_dir += 1
        return res