class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        res = [[0]*n for i in range(m)]
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]

        for i in range(m):
            for j in range(n):

                neighs = 0
                curr_sum = 0
                for direc in directions:
                    if i+direc[0]>=0 and i+direc[0]<m and j+direc[1]>=0 and j+direc[1]<n:
                        neighs += 1
                        curr_sum += img[i+direc[0]][j+direc[1]]
                        
                    
                res[i][j] = curr_sum//neighs
        return res