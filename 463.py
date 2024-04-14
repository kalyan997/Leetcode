class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def isValidCoor(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        perimeter = 0

        def curr_perimeter(i,j):
            res = 4
            for dir in directions:
                next_r, next_c = i+dir[0], j+dir[1]
                if isValidCoor(next_r,next_c) and grid[next_r][next_c]==1:
                    res -= 1
            
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    
                    perimeter += curr_perimeter(i,j)
                    
        return perimeter