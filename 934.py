class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        my_q = deque()

        def isValidCoor(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True

        visited = set()
        def dfs(i,j):
            if not isValidCoor(i,j) or grid[i][j]==0:
                return
            grid[i][j] = 0
            visited.add((i,j))
            my_q.append([i,j,0])
            for curr_dir in directions:
                next_i, next_j = i+curr_dir[0],j+curr_dir[1]
                dfs(next_i, next_j)



        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    found = True
                    my_q.append([i,j])
                    #grid[i][j] = 0
                    break
            if found == True:
                break
        #print(my_q)

        curr = my_q.popleft()
        first_i, first_j = curr[0], curr[1]

        dfs(first_i, first_j)
        #print(my_q)
        found = False
        res = 0
        while my_q:
            #print(my_q)
            curr_size = len(my_q)

            for i in range(curr_size):
                curr = my_q.popleft()
                curr_i, curr_j, curr_val = curr[0], curr[1], curr[2]

                for curr_dir in directions:
                    next_i, next_j = curr_i+curr_dir[0],curr_j+curr_dir[1]
                    if isValidCoor(next_i, next_j) and grid[next_i][next_j]==1:
                        res = curr_val
                        found = True
                        break
                    if isValidCoor(next_i, next_j) and (next_i,next_j) not in visited:
                        my_q.append([next_i,next_j,curr_val+1])
                        visited.add((next_i,next_j))
                if found==True:
                    break
            if found==True:
                    break
        
        return res