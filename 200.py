class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        def isValidCoor(i,j):
            if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]):
                return False
            return True

        def bfs(curr_row,curr_col):
            my_q = deque()
            my_q.append([curr_row,curr_col])
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            grid[curr_row][curr_col] = "0"
            while my_q:
                curr_pos = my_q.popleft()
                curr_row, curr_col = curr_pos[0], curr_pos[1]
                
                for dir in directions:
                    next_row, next_col = curr_row+dir[0], curr_col+dir[1]
                    if isValidCoor(next_row,next_col) and grid[next_row][next_col]=="1":
                        my_q.append([next_row,next_col])
                        grid[next_row][next_col] = "0"

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    num_islands += 1
                    bfs(i,j)
        return num_islands


