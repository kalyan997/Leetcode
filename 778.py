class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        max_in_minPath = 0
        n = len(grid)
        

        def isValidCoor(i,j):
            if i<0 or j<0 or i>=n or j>=n:
                return False
            return True

        low = grid[0][0]
        high = n*n
        
        def PathExists(val):
            visited = set()
            return dfs(0,0,val,visited)
    
        def dfs(i,j,val,visited):
            visited.add((i,j))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            if i==n-1 and j==n-1:
                return True
            for dir in directions:
                next_row, next_col = i+dir[0], j+dir[1]
                if isValidCoor(next_row, next_col) and (next_row,next_col) not in visited and grid[next_row][next_col]<=val:
                    if dfs(next_row, next_col, val,visited):
                        return True
            return False

        print(PathExists(19))
        while low<high:
            mid = low + (high-low)//2
            print(mid, PathExists(mid))
            if PathExists(mid):
                high = mid
            else:
                low = mid+1
                
        return low