class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValidCoor(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return False
            return True

        rows, cols = len(grid), len(grid[0])
        my_q = deque()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    my_q.append([i,j])
                    grid[i][j] = 3
                if grid[i][j]==1:
                    fresh_oranges+=1

        time_elapsed = 0
        while my_q:
            print(my_q)
            curr_size = len(my_q)
            time_elapsed += 1
            for i in range(curr_size):
                curr = my_q.popleft()
                row,col = curr[0],curr[1]
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dir in directions:
                    next_row = row+dir[0]
                    next_col = col+dir[1]
                    if isValidCoor(next_row,next_col) and grid[next_row][next_col]==1:
                        grid[next_row][next_col] = 3
                        my_q.append([next_row,next_col])
        print(grid)
        print(time_elapsed)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        
        return time_elapsed-1 if fresh_oranges!=0 else 0