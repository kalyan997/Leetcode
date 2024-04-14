class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])        
        start = [-1,-1]
        end = [-1,-1]
        
        obstacles = set()
        num_obstacles = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == -1:
                    obstacles.add((i,j))
                    num_obstacles += 1
                elif grid[i][j] == 2:
                    end = [i,j]
        
        print(end)
        req_path_len = m*n-num_obstacles
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def is_valid_coor(i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True
        
        visited = set()
        res = 0

        def dfs(i,j,visited, path_len):
            
            nonlocal res
            print(i,j, path_len, res)
            if i==end[0] and j == end[1]:
                
                #path_len -= 1
                #visited.remove((i,j))
                if path_len == req_path_len:
                    print(i,j)
                    res += 1
                return
                
            for curr_dir in directions:
                
                if is_valid_coor(i+curr_dir[0], j+curr_dir[1]) and (i+curr_dir[0], j+curr_dir[1]) not in obstacles and (i+curr_dir[0], j+curr_dir[1]) not in visited:
                    
                    visited.add((i,j))
                    dfs(i+curr_dir[0], j+curr_dir[1], visited, path_len+1)
                    #path_len -= 1
                    visited.remove((i,j))
                    
        visited.add((start[0], start[1]))
        path_len = 1
        dfs(start[0], start[1], visited, path_len)
        
        return res