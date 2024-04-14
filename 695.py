class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValidCoor(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return False
            return True

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    curr_area = 0
                    my_q = deque()
                    my_q.append([i,j])
                    while my_q:
                        curr = my_q.popleft()
                        print(curr)
                        grid[curr[0]][curr[1]]=2
                        curr_area += 1
                        row, col = curr[0], curr[1]
                        directions = [[1,0],[-1,0],[0,1],[0,-1]]
                        for dir in directions:
                            next_row = row+dir[0]
                            next_col = col+dir[1]
                            if isValidCoor(next_row,next_col) and grid[next_row][next_col]==1:
                                grid[next_row][next_col]=2          
                                my_q.append([next_row,next_col])
                        max_area = max(curr_area, max_area)
                    print(i,j,curr_area)
        return max_area